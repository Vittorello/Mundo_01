from random import choice
from time import sleep

try:
    valor = int(input("Tente adivinhar o número que estou pensando, entre 0 e 5: "))
    print("Analisando seu número...")
    num = range(0,5)
    numero = choice(num)
    sleep(3)

    if valor == numero:
        print(f"Parabéns! Você acertou! O número era {numero}.")

    elif valor < 0 or valor > 5:
        print("Digite um número válido!")

    else:
        print(f"Que pena, você errou. O número correto era {numero}. Tente novamente!")

except ValueError:
    print("Erro: Você deve inserir valores numéricos válidos.")
    exit()