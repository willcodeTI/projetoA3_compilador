from classifier import ProgrammingLanguageClassifier
 
 
EXAMPLES = {
    "Python": "def hello():\n    print('Hello')",
    "JavaScript": "const hello = () => console.log('Hello');",
    "Java": "public static void main(String[] args) { }",
    "C": "#include <stdio.h>\nint main() { printf('Hello'); }",
    "Kotlin": "fun main() { println('Hello') }",
}
 
 
def show_examples(classifier: ProgrammingLanguageClassifier) -> None:
    print("\n" + "=" * 60)
    print("EXEMPLOS")
    print("=" * 60)
 
    for lang, code in EXAMPLES.items():
        predicted, score = classifier.predict(code)
        print(f"\n{lang}:")
        print(f"  Codigo: {code}")
        print(f"  Detectado: {predicted} (score: {score})")
 
 
def show_result(scores: dict, predicted: str, score: int) -> None:
    print("\n" + "=" * 60)
    print(f"RESULTADO: {predicted.upper()}")
    print(f"Score: {score}")
    print("=" * 60)
    print("Scores por linguagem:")
    for lang in sorted(scores.keys(), key=lambda x: scores[x], reverse=True):
        bar = "#" * (scores[lang] // 10)
        print(f"  {lang:12} : {scores[lang]:3} {bar}")
    print("=" * 60)