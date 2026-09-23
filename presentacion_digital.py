tarjeta_presentacion = {
    "nombre": input("Ingrese su nombre: "),
    "edad": int(input("Ingrese su edad: ")),
    "ciudad": input("Ingrese su ciudad: "),
}
print("hola, mi nombre es " + tarjeta_presentacion["nombre"] + ", tengo " + str(tarjeta_presentacion["edad"]) + " años y vivo en " + tarjeta_presentacion["ciudad"] + ".")
print(" el proximo año tendre " + str(tarjeta_presentacion["edad"] + 1) + " años.")