edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("edad invalida")
elif edad <= 11:
    print("categoria: infancia")
elif edad <= 17:
    print("categoria: adolescencia")
elif edad <= 59:
    print("categoria: adultez")
else :
    print("categoria: adulto mayor")