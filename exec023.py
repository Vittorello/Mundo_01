cidade = str(input("Digite o nome da sua cidade: ")).strip()

if cidade.lower().startswith("santo"):
    print("Tem 'Santo' no nome da cidade.")
else:
    print("Não tem 'Santo' no nome da cidade")