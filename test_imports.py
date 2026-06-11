#!/usr/bin/env python
"""
Script de teste para validar a estrutura e imports do projeto.
Execute: python test_imports.py
"""

import sys
from pathlib import Path

def test_imports():
    """Testa se todos os imports funcionam corretamente."""

    print("=" * 60)
    print("Testando Imports da Estrutura")
    print("=" * 60)

    # Adiciona src ao path (simula o que streamlit_app.py faz)
    project_root = Path(__file__).parent
    src_path = project_root / "src"
    sys.path.insert(0, str(src_path))

    print(f"\nDiretorio do projeto: {project_root}")
    print(f"Adicionado ao path: {src_path}")
    print(f"Path existe: {src_path.exists()}")

    # Testa imports
    tests = [
        ("classifier", "ProgrammingLanguageClassifier"),
        ("patterns", "python_patterns"),
        ("utils", "show_examples"),
        ("main", "main"),
    ]

    print("\n" + "-" * 60)
    print("Testando imports:")
    print("-" * 60)

    all_passed = True

    for module, item in tests:
        try:
            if module == "main":
                __import__(module)
                print(f"[OK] import {module}")
            else:
                mod = __import__(module)
                getattr(mod, item)
                print(f"[OK] from {module} import {item}")
        except Exception as e:
            print(f"[ERRO] from {module} import {item}")
            print(f"       {e}")
            all_passed = False

    print("\n" + "-" * 60)

    if all_passed:
        print("[SUCESSO] TODOS OS IMPORTS FUNCIONAM!")
        print("-" * 60)
        print("\nVoce pode executar:")
        print("  streamlit run app/streamlit_app.py")
        return 0
    else:
        print("[FALHA] ALGUNS IMPORTS FALHARAM")
        return 1

if __name__ == "__main__":
    sys.exit(test_imports())
