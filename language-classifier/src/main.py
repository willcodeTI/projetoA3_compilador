from classifier import ProgrammingLanguageClassifier
from Utils import show_examples, show_result


def main():
    classifier = ProgrammingLanguageClassifier()
 
    print("=" * 60)
    print("CLASSIFICADOR DE LINGUAGEM DE PROGRAMACAO")
    print("=" * 60)
    print("Digite 'sair' para finalizar")
    print("Digite 'exemplo' para ver exemplos")
    print("=" * 60)
 
    while True:
        print("\nDigite seu codigo (termine com uma linha vazia):")
        lines = []
 
        try:
            while True:
                line = input()
                if line.lower() == 'sair':
                    print("Encerrando...")
                    return
                if line.lower() == 'exemplo':
                    show_examples(classifier)
                    print("\nDigite seu codigo (termine com uma linha vazia):")
                    continue
                if line == "":
                    break
                lines.append(line)
        except EOFError:
            break
 
        code = "\n".join(lines)
 
        if not code.strip():
            print("Nenhum codigo foi digitado. Tente novamente.")
            continue
 
        predicted, score = classifier.predict(code)
        scores = classifier.classify(code)
 
        show_result(scores, predicted, score)
 
 
if __name__ == "__main__":
    main()
