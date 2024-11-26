import calendar

while True:
    try:
        ano = int(input("Digite o ano que voê quer saber se é bisssexto ou não: "))
        if calendar.isleap(ano):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"Esse ano {ano} não é bissexto")
        break
    except ValueError:
        print("Digite um ano válido.")