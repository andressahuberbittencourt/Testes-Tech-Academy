numero = int(input("Digite n: "))

Cont = 1
Fatorial = numero
while Cont < numero :
    Fatorial = Fatorial * (numero - Cont)
    Cont = Cont + 1
print ("O fatorial de", numero, "é", Fatorial)