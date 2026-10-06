numero_primo = int(input("ingrese un numero para verificar si es primo: "))
if numero_primo <= 1:
    print(numero_primo, "no es un numero primo")
if numero_primo > 1:
    for i in range(2, numero_primo):
        if (numero_primo % i) == 0:
            print(numero_primo, "no es un numero primo", i, "es un divisor")
            break
    else:
        print(numero_primo, "es un numero primo")