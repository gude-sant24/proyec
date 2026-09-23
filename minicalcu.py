operacion = input("seleccione el calculo a operar: +, -, *, /")
if operacion == "+":
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    print("el resultado de la suma es: " + str(num1 + num2))
elif operacion == "-":
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    print("el resultado de la resta es: " + str(num1 - num2))
elif operacion == "*":
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    print("el resultado de la multiplicacion es: " + str(num1 * num2))
elif operacion == "/":
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    if num2 == 0:
        print("error no se puede dividir entre 0")
    else :
        print("el resultado de la division es: " + str(num1 / num2))