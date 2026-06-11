# Guia de Uso - Interface Streamlit

## Instalacao

1. Navegue até o diretório `language-classifier`:
```bash
cd language-classifier
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executar a Aplicacao

Na pasta `language-classifier`, execute:
```bash
streamlit run app.py
```

A interface abrirá automaticamente em `http://localhost:8501`

## Funcionalidades

### Aba "Classificar"
- Cole seu código no campo de texto
- Clique em "Classificar"
- Veja o resultado com:
  - Linguagem detectada
  - Score (pontuação)
  - Confiança da classificação
  - Gráfico com distribuição de scores

### Aba "Exemplos"  
- Veja exemplos de cada linguagem
- Clique em "Testar [Linguagem]" para testar

### Aba "Sobre"
- Informações sobre como o classificador funciona
- Linguagens suportadas
- Dicas para melhores resultados

## Opcoes

Na aba de classificação:
- **Mostrar detalhes**: Exibe análise profunda dos padrões encontrados
- **Mostrar grafico**: Visualiza os scores em gráfico interativo
