ahorro_mensual = int(input("ingrese el ahorro mensual "))
cant_meses = int(input("ingrese el numero de meses en los cuales ahorro "))
if cant_meses <= 0 :
    print("error, la cantidad de meses debe ser mayor a 0")
else :
    for i in range (1, cant_meses + 1) :
        print("mes" + str(i) + ":" + str(ahorro_mensual * i))

    
