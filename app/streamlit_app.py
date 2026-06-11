import streamlit as st
import sys
from pathlib import Path

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from classifier import ProgrammingLanguageClassifier
import plotly.graph_objects as go

st.set_page_config(
    page_title="Classificador de Linguagem",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-title {
        font-size: 2.5em;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 20px 0;
    }
    .language-badge {
        display: inline-block;
        padding: 10px 20px;
        border-radius: 50px;
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
        font-size: 1.2em;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_classifier():
    return ProgrammingLanguageClassifier()

classifier = load_classifier()

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown('<div class="main-title">🔍 Classificador de Linguagem</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Detecte automaticamente a linguagem do seu código</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📝 Classificar", "📚 Exemplos", "ℹ️ Sobre"])

with tab1:
    col1, col2 = st.columns([3, 1])

    with col1:
        code_input = st.text_area(
            "Cole seu código aqui:",
            height=300,
            placeholder="// Insira o código que deseja classificar...\n\nfunction hello() {\n  console.log('Hello, World!');\n}",
            label_visibility="visible"
        )

    with col2:
        st.markdown("### Opcoes")
        show_details = st.checkbox("Mostrar detalhes", value=True)
        show_chart = st.checkbox("Mostrar grafico", value=True)

    if st.button("Classificar", use_container_width=True, type="primary"):
        if code_input.strip():
            predicted, score = classifier.predict(code_input)
            scores = classifier.classify(code_input)

            st.markdown(f'<div class="result-box">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([2, 1, 2])

            with col2:
                st.markdown(f'<div class="language-badge">{predicted}</div>', unsafe_allow_html=True)

            with col1:
                st.metric("Score", f"{score}", delta=None)

            with col3:
                sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
                second_lang = sorted_scores[1][0] if len(sorted_scores) > 1 else "N/A"
                second_score = sorted_scores[1][1] if len(sorted_scores) > 1 else 0
                confidence = ((score - second_score) / max(score, 1)) * 100
                st.metric("Confianca", f"{confidence:.1f}%")

            st.markdown('</div>', unsafe_allow_html=True)

            if show_chart:
                st.markdown("### Distribuicao de Scores")

                fig = go.Figure()

                sorted_langs = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)
                colors = ['#FF6B6B' if lang == predicted else '#4ECDC4' for lang in sorted_langs]

                fig.add_trace(go.Bar(
                    x=sorted_langs,
                    y=[scores[lang] for lang in sorted_langs],
                    marker=dict(color=colors),
                    text=[f"{scores[lang]}" for lang in sorted_langs],
                    textposition="outside",
                    hovertemplate="<b>%{x}</b><br>Score: %{y}<extra></extra>"
                ))

                fig.update_layout(
                    title="Scores por Linguagem",
                    xaxis_title="Linguagem",
                    yaxis_title="Score",
                    showlegend=False,
                    height=400,
                    hovermode='x unified'
                )

                st.plotly_chart(fig, use_container_width=True)

            if show_details:
                st.markdown("### Scores Detalhados")

                col1, col2, col3, col4, col5 = st.columns(5)
                cols = [col1, col2, col3, col4, col5]

                for i, (lang, score) in enumerate(sorted(scores.items(), key=lambda x: x[1], reverse=True)):
                    with cols[i]:
                        st.metric(lang, score)

                with st.expander("Analise Detalhada"):
                    scores_debug, details = classifier.classify_debug(code_input)

                    for lang in sorted(details.keys(), key=lambda x: scores_debug[x], reverse=True):
                        if details[lang]:
                            st.markdown(f"**{lang}** - Total: {scores_debug[lang]} pontos")

                            details_html = "<ul>"
                            for pattern, count, points in details[lang][:5]:
                                details_html += f"<li>{pattern} = {count}x encontrado ({points} pt cada)</li>"
                            if len(details[lang]) > 5:
                                details_html += f"<li>... e mais {len(details[lang]) - 5}</li>"
                            details_html += "</ul>"

                            st.markdown(details_html, unsafe_allow_html=True)
        else:
            st.warning("Por favor, insira algum codigo para classificar!")

with tab2:
    st.markdown("### Exemplos de Cada Linguagem")

    EXAMPLES = {
        "Python": "def hello():\n    print('Hello, World!')\n\nhello()",
        "JavaScript": "const hello = () => console.log('Hello, World!');\nhello();",
        "Java": "public class Hello {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}",
        "C": "#include <stdio.h>\nint main() {\n    printf(\"Hello, World!\");\n    return 0;\n}",
        "Kotlin": "fun main() {\n    println(\"Hello, World!\")\n}",
    }

    cols = st.columns(2)

    for idx, (lang, code) in enumerate(EXAMPLES.items()):
        with cols[idx % 2]:
            with st.container(border=True):
                st.markdown(f"### {lang}")
                st.code(code, language=lang.lower())

                if st.button(f"Testar {lang}", key=f"btn_{lang}", use_container_width=True):
                    predicted, score = classifier.predict(code)
                    scores = classifier.classify(code)

                    st.success(f"Detectado: **{predicted}** (Score: {score})")

                    col1, col2, col3, col4, col5 = st.columns(5)
                    cols_metrics = [col1, col2, col3, col4, col5]

                    for i, (l, s) in enumerate(sorted(scores.items(), key=lambda x: x[1], reverse=True)):
                        with cols_metrics[i]:
                            st.metric(l, s)

with tab3:
    st.markdown("""
    ### Sobre o Classificador

    Este classificador de linguagens de programacao usa **padroes de regex** para identificar a linguagem
    mais provavel de um trecho de codigo.

    #### Como Funciona

    1. **Analise de Padroes**: O classificador busca padroes caracteristicos de cada linguagem
    2. **Calculo de Pontuacao**: Cada padrao encontrado contribui com pontos a sua linguagem
    3. **Resultado Final**: A linguagem com a maior pontuacao e indicada como resultado

    #### Linguagens Suportadas

    - **Python** - Caracteristicas: `def`, `print()`, indentacao
    - **JavaScript** - Caracteristicas: `const`, `function`, `console.log()`
    - **Java** - Caracteristicas: `class`, `public static void`, `String[]`
    - **C** - Caracteristicas: `#include`, `void`, `printf()`
    - **Kotlin** - Caracteristicas: `fun`, `println()`, type inference

    #### Interpretando os Resultados

    - **Score**: Pontuacao total da linguagem detectada
    - **Confianca**: Diferenca percentual entre o 1 e 2 lugar
    - **Distribuicao**: Mostra como o codigo se encaixa em cada linguagem

    #### Limitacoes

    - Fragmentos muito pequenos podem ter resultados imprecisos
    - Codigo misto ou hibrido pode ter resultados ambiguos
    - Padroes simples podem aparecer em multiplas linguagens

    ---

    **Desenvolvido com amor usando Streamlit**
    """)

    st.markdown("### Feedback")
    st.info("Se encontrar alguma classificacao incorreta, tente adicionar mais contexto ao codigo!")
