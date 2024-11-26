from time import sleep

try:
    velocidade = int(input("Digite a velocidade do veículo: "))
    limite = 80
    multa = 7
    sleep(2)

    if velocidade > limite:
        print(f"A velocidade permitida na via é {limite}Km/h. Sua velocidade foi de {velocidade}Km/h. Você foi multado!")
        print(f"Você está a {velocidade - limite}Km/h acima da velocidade permitida!")
        print(f"A sua multa será no valor de R${(velocidade - limite) * multa}")

    elif velocidade <0:
        print("Digite uma quilometragem positiva.")

    else:
        print(f"Você está dentro da velocidade permitida. Sua velocidade é {velocidade}Km/h")
except ValueError:
    print("Digite uma quilometragem correta.")