

from ast import If


a = int(input("Digite a nota A:"))
b = int(input("Digite a nota B:"))
c = int(input("Digite a nota C:"))

MEDIA = ((a * 2) + b + (c * 2)) /  5
if (MEDIA >= 6):
    print("APROVADO")
else:
    if  MEDIA >= 3:
        print("RECUPERAÇÃO")
    else:
        print("REPROVADO")
