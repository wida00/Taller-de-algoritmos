import math
numero=float(input("Ingrese un número decimal: "))
binario=""
if numero>0:
    while numero>0:
        if numero%2==0:
            binario="0"+binario
        else:
            binario="1"+binario
        numero=int(math.floor(numero/2))
else:
    if numero==0:
        binario="0"
    else:
        binario="no se puede convertir el  número. Ingrese solo"

print("El número convertido es, "+binario)