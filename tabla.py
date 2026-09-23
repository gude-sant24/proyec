numero_multiplicacion = int(input("ingrese el numero a multiplicar "))
tabla = int(input("ingrese las veces que se va a multiplicar "))
for i in range(1, tabla + 1):
    print(str(numero_multiplicacion) + "x" + str(i) + "=" + str(numero_multiplicacion * i))