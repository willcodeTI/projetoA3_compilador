import re
from typing import Dict, Tuple

from patterns import (
    python_patterns,
    javascript_patterns,
    java_patterns,
    c_patterns,
    kotlin_patterns,
)


class ProgrammingLanguageClassifier:
    def __init__(self):
        self.languages = {
            'Python': python_patterns(),
            'JavaScript': javascript_patterns(),
            'Java': java_patterns(),
            'C': c_patterns(),
            'Kotlin': kotlin_patterns(),
        }

    def classify_debug(self, code: str) -> Tuple[Dict[str, int], Dict[str, list]]:
        scores = {lang: 0 for lang in self.languages}
        details = {lang: [] for lang in self.languages}

        for language, patterns in self.languages.items():
            for pattern, points in patterns:
                matches = re.findall(pattern, code, re.MULTILINE)
                if matches:
                    count = len(matches)
                    scores[language] += count * points
                    details[language].append((pattern, count, points))

        return scores, details

    def classify(self, code: str) -> Dict[str, int]:
        scores, _ = self.classify_debug(code)
        return scores

    def predict(self, code: str) -> Tuple[str, int]:
        scores = self.classify(code)
        best_language = max(scores, key=scores.get)
        return best_language, scores[best_language]

