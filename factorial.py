numero = int(input("ingrese su numero "))
factorial = 1
if numero <=0 :
    print ("error")
else :
    secuencia = str(numero)
    for i in range (numero,0,-1) :
        factorial_resultante = factorial * i
        factorial = factorial_resultante
        if i == numero :
            secuencia = str(i)
        else :
            secuencia = secuencia + "*" + str(i)
        print(str(numero) + "!" + "=" + secuencia + "=" + str(factorial))
    


    

