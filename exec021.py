nome = str(input("Digite seu nome: "))

print(f'nome em maiúsculo: {nome.upper()}')
print(f'nome em minusculo: {nome.lower()}')
print(len(nome.replace(" ","")))
print(len(nome.split()[0]))