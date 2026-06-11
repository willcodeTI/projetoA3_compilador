from typing import Tuple
 
 
def python_patterns() -> list[Tuple[str, int]]:
    return [
        (r'def\s+\w+', 20),
        (r'class\s+\w+', 20),
        (r'import\s+', 15),
        (r'from\s+.+\s+import', 15),
        (r'if\s+__name__', 25),
        (r':\s*$', 10),
        (r'for\s+\w+\s+in\s+', 15),
        (r'with\s+', 15),
        (r'@', 12),
        (r'print\s*\(', 15),
        (r'elif', 10),
        (r'lambda', 15),
    ]
 
 
def javascript_patterns() -> list[Tuple[str, int]]:
    return [
        (r'function\s+\w+', 20),
        (r'const\s+\w+', 18),
        (r'let\s+\w+', 18),
        (r'var\s+\w+', 15),
        (r'=>', 20),
        (r'console\.', 15),
        (r'require\s*\(', 18),
        (r'export\s+', 15),
        (r'this\.', 10),
        (r'async\s+', 15),
        (r'await\s+', 15),
        (r'\.then\s*\(', 12),
    ]
 
 
def java_patterns() -> list[Tuple[str, int]]:
    return [
        (r'public\s+', 15),
        (r'class\s+\w+', 25),
        (r'static\s+', 15),
        (r'System\.out', 20),
        (r'new\s+\w+', 12),
        (r'import\s+', 15),
        (r'private\s+', 10),
        (r'void\s+', 15),
        (r'String\[\]', 15),
        (r'@Override', 15),
        (r'extends\s+', 15),
        (r'implements\s+', 15),
    ]
 
 
def c_patterns() -> list[Tuple[str, int]]:
    return [
        (r'#include', 25),
        (r'int\s+main', 25),
        (r'printf', 20),
        (r'malloc', 20),
        (r'free\s*\(', 15),
        (r'struct\s+', 18),
        (r'void\s+', 15),
        (r'#define', 15),
        (r'\*\s*\w+', 10),
        (r'scanf', 15),
        (r'FILE\s*\*', 15),
        (r'fopen', 15),
    ]
 
 
def kotlin_patterns() -> list[Tuple[str, int]]:
    return [
        (r'fun\s+\w+', 25),
        (r'val\s+\w+', 20),
        (r'var\s+\w+', 20),
        (r'data\s+class', 20),
        (r'->', 18),
        (r'class\s+\w+', 15),
        (r'println', 12),
        (r'launch\s*{', 10),
        (r'\.let\s*{', 12),
        (r'\?\.', 8),
        (r'suspend\s+', 15),
        (r'coroutine', 15),
    ]