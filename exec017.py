import math

angulo = int(input("Ângulo: "))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f"Radiano = {rad:.2f} \nSeno = {seno:.2f} \nCosseno = {cosseno:.2f} \nTangente = {tangente:.2f}")