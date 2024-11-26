frase = str(input("Digite uma frase: ")).lower().strip()

print(f"A letra 'A' aparece {frase.count('a')} vezes")
print(f"A letra aparece a primeira vez no {int(frase.find("a")) + 1} da string")
print(f"A letra aparece a última vez no {int(frase.rfind("a")) + 1} da string")