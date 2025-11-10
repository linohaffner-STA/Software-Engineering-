# app.py - Python SonarQube Demo
# Enthält Bugs, Sicherheitslücken und Code-Smells für die Analyse

import math

def calculate_area(radius):
    # Fehler: keine Typprüfung, kann mit Strings crashen
    return math.pi * radius * radius

def divide(a, b):
    # Mögliche Division durch Null
    return a / b

def insecure_input():
    # Kritisch: eval() auf Benutzereingaben
    data = input("Enter math expression: ")
    return eval(data)

def unused_function(x, y):
    # Nie verwendet - Code Smell
    return x + y

def main():
    print("SonarQube Python Demo")
    print("Fläche:", calculate_area("5"))  # absichtlich falscher Typ
    print("Division:", divide(5, 0))
    print(insecure_input())

if __name__ == "__main__":
    main()
