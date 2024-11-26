from calendar import isleap
from datetime import date

while True:
    try:
        ano = int(input("Digite o ano que você quer analisar ou digite 0 para analisar o ano atual: "))
        if ano == 0:
            ano = date.today().year
        if isleap(ano):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"Esse ano {ano} não é bissexto")
        break
    except ValueError:
        print("Digite um ano válido.")