import math

cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)

print(f"De acordo com os catetos inseridos, a hipotenusa é {hipotenusa:.2f}")