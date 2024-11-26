lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print(f"{lado1}, {lado2}, {lado3} formam um triângulo.")
else:
    print(f"{lado1}, {lado2}, {lado3} não formam um triângulo.")