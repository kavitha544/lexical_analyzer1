Lexical Analyzer & Token Counter

This project implements a Lexical Analyzer and Token Counter in Python that reads a C source file and identifies different types of tokens.

Token Types
Keywords
Identifiers
Operators
Constants
String Literals
Separators
Comments
Special Symbols
Files
Lexical-Analyzer/
├── first_follow.c
├── lexical_analyzer.py
└── README.md
first_follow.c – C program for finding FIRST and FOLLOW sets.
lexical_analyzer.py – Python program that analyzes the C code and counts tokens.
README.md – Project documentation.
Sample C Program

The C program used for token analysis is the FIRST and FOLLOW program.

How to Run

Open the terminal in the project folder and run:

python lexical_analyzer.py

If required:

python3 lexical_analyzer.py
Output

The program displays each token with its type and provides the total token count for each category.

Technologies

Python, C, Regular Expressions
