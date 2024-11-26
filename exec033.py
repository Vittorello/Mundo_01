while True:
    try:
        salario = float(input("Digite seu salário: "))

        if salario > 1250:
            resultado = salario * 0.10
            print(f"Seu aumento é de R${resultado:.2f} e seu salário será de R${salario + resultado:.2f}")

        elif salario < 0:
            print("Digite um salário positivo.")

        elif salario <= 1250:
            resultado = salario * 0.15
            print(f"Seu aumento é de R${resultado:.2f} e seu salário será de R${salario + resultado:.2f}")
            break
        else:
            print("Você não irá receber o aumento")

    except ValueError:
        print("Digite o salário válido.")
