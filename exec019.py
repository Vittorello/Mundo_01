import random

nome = ['Igor','Lucas','Ana','Maysa']

random.shuffle(nome)

for i,nome in enumerate(nome,start = 1):
    print(f"{i} - {nome}")