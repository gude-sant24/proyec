numero = int(input("ingrese su numero "))
factorial = 1
if numero <=0 :
    print ("error")
else :
    for i in range (factorial, numero + 1) :
        factorial_resultante = factorial * i
        factorial = factorial_resultante
        print (factorial)


