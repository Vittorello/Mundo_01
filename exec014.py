km = float(input("Digite quantos km você rodou com o carro: "))
dias = int(input("Digite quantos dias você alugou o carro: "))
pago = (dias * 60) + (km * 0.15)

print(f"O total a se pagar pelo aluguel do carro é R${pago}")