# Estrutura do Projeto Reorganizada

## Nova Estrutura

A estrutura do projeto foi reorganizada para seguir as melhores práticas profissionais:

```
compilador-A3/
├── README.md                      # Documentação principal
├── requirements.txt               # Dependências
├── .gitignore                     # Configuração Git
├── .env.example                   # Variáveis de ambiente exemplo
│
├── src/                          # Código da lógica
│   ├── __init__.py
│   ├── classifier.py             # Classificador principal
│   ├── patterns.py               # Padrões de linguagens
│   ├── utils.py                  # Utilidades
│   └── main.py                   # Script CLI
│
├── app/                          # Interface web
│   ├── __init__.py
│   └── streamlit_app.py          # Aplicação Streamlit
│
├── docs/                         # Documentação
│   ├── PROJECT_README.md         # README original
│   └── STREAMLIT_GUIDE.md        # Guia de uso
│
├── scripts/                      # Scripts de execução
│   ├── run.bat                   # Windows
│   └── run.sh                    # Linux/Mac
│
└── tests/                        # Testes (futuro)
```

## Mudanças Realizadas

✅ **Criados:**
- `src/` - Código principal organizado
- `app/` - Interface Streamlit
- `docs/` - Documentação centralizada
- `scripts/` - Scripts de execução
- `tests/` - Diretório para testes
- `.gitignore` - Configuração profissional do Git
- `.env.example` - Exemplo de variáveis de ambiente
- `src/__init__.py` e `app/__init__.py` - Pacotes Python

✅ **Reorganizados:**
- `classifier.py` → `src/classifier.py`
- `patterns.py` → `src/patterns.py`
- `Utils.py` → `src/utils.py`
- `main.py` → `src/main.py`
- `app.py` → `app/streamlit_app.py`
- `run.bat` e `run.sh` → `scripts/`
- Documentação → `docs/`

## Próximos Passos

⚠️ **A pasta `language-classifier/` pode ser removida quando:**
1. Não houver mais processos Streamlit rodando
2. Você estiver certo de que não precisa dos arquivos antigos

Para remover:
```bash
rm -rf language-classifier/
```

## Como Usar

### Executar a Interface Web
```bash
# Windows
scripts/run.bat

# Linux/Mac
bash scripts/run.sh

# Manualmente
streamlit run app/streamlit_app.py
```

### Usar o Script CLI
```bash
python -m src.main
```

## Instalação de Dependências

```bash
pip install -r requirements.txt
```

---

**Estrutura profissional implementada com sucesso!** ✨
