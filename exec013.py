nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salário: "))
bonus = salario * 0.15
novo_salario = salario + bonus

print(f"Parabéns {nome}, esse é o seu novo salário {novo_salario:.2f}")