try:
    km_viagem = int(input("Digite a quilometragem da sua viagem: "))

    if km_viagem <= 200:
        print(f"Esse será o valor da sua passagem, de acordo com o KM R${km_viagem * 0.50}")
    elif km_viagem > 200:
        print(f"Esse será o valor da sua passagem, de acordo com o KM R${km_viagem * 0.45}")
    else:
        print("O valor da viagem será cobrado normalmente.")
except ValueError:
    print("Digite uma quilometragem válida.")