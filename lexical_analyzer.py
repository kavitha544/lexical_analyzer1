import re
from collections import Counter

# Read C source code
with open("first.c", "r") as file:
    code = file.read()

keywords = {
    "auto", "break", "case", "char", "const", "continue",
    "default", "do", "double", "else", "enum", "extern",
    "float", "for", "goto", "if", "int", "long", "register",
    "return", "short", "signed", "sizeof", "static", "struct",
    "switch", "typedef", "union", "unsigned", "void", "volatile",
    "while"
}

operators = {
    "+", "-", "*", "/", "%", "=", "==", "!=", "<", ">",
    "<=", ">=", "++", "--", "&&", "||", "!"
}

separators = {
    "(", ")", "{", "}", "[", "]", ";", ",", ":"
}

counts = Counter()

# Find comments
comments = re.findall(r'//.*|/\*[\s\S]*?\*/', code)

for comment in comments:
    print(comment, "-> Comment")
    counts["Comments"] += 1

# Remove comments
code = re.sub(r'//.*|/\*[\s\S]*?\*/', '', code)

# Find preprocessor directive
preprocessor = re.findall(r'#include\s*<[^>]+>', code)

for item in preprocessor:
    print(item, "-> Special Symbol")
    counts["Special Symbols"] += 1

code = re.sub(r'#include\s*<[^>]+>', '', code)

# Token pattern
pattern = r'"[^"]*"|<=|>=|==|!=|\+\+|--|&&|\|\||[+\-*/%=<>!]|[(){}\[\];,:]|\d+(?:\.\d+)?|[A-Za-z_]\w*'

tokens = re.findall(pattern, code)

print("\nTOKEN TYPE")
print("-" * 40)

for token in tokens:

    if token.startswith('"'):
        token_type = "String Literal"
        counts["String Literals"] += 1

    elif token in keywords:
        token_type = "Keyword"
        counts["Keywords"] += 1

    elif token in operators:
        token_type = "Operator"
        counts["Operators"] += 1

    elif token in separators:
        token_type = "Separator"
        counts["Separators"] += 1

    elif token.isdigit():
        token_type = "Constant"
        counts["Constants"] += 1

    else:
        token_type = "Identifier"
        counts["Identifiers"] += 1

    print(f"{token:<20} {token_type}")

# Display token count
print("\n" + "-" * 40)
print("Token Count")

print("Keywords        :", counts["Keywords"])
print("Identifiers     :", counts["Identifiers"])
print("Operators       :", counts["Operators"])
print("Constants       :", counts["Constants"])
print("String Literals :", counts["String Literals"])
print("Separators      :", counts["Separators"])
print("Comments        :", counts["Comments"])
print("Special Symbols :", counts["Special Symbols"])