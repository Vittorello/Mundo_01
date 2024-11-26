nome = str(input("Digite seu nome: "))

nome = nome.lower().split()
if "silva" in nome:
    print("Contem 'silva no seu nome'.")
else:
    print("Não contem 'silva' no seu nome.")