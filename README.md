# Programming Language Classifier

Um classificador automático de linguagens de programação usando análise de padrões regex com interface Streamlit.

## 📋 Estrutura do Projeto

```
compilador-A3/
├── README.md                      # Este arquivo
├── requirements.txt               # Dependências do projeto
│
├── src/                          # Código principal
│   ├── __init__.py
│   ├── classifier.py             # Classe principal
│   ├── patterns.py               # Padrões de cada linguagem
│   ├── utils.py                  # Funções utilitárias
│   └── main.py                   # Script CLI
│
├── app/                          # Interface Streamlit
│   ├── __init__.py
│   └── streamlit_app.py          # Aplicação web
│
├── docs/                         # Documentação
│   ├── PROJECT_README.md         # README original
│   └── STREAMLIT_GUIDE.md        # Guia Streamlit
│
└── scripts/                      # Scripts de execução
    ├── run.bat                   # Windows
    └── run.sh                    # Linux/Mac
```

## 🚀 Quick Start

### Instalação
```bash
pip install -r requirements.txt
```

### Interface Web (Streamlit)
```bash
streamlit run app/streamlit_app.py
```

### Script CLI
```bash
python -m src.main