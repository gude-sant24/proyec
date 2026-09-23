ancho_pared = float(input("Ingrese el ancho de la pared en metros: "))
alto_pared = float(input("Ingrese el alto de la pared en metros: "))
area = ancho_pared * alto_pared
rendimiento = float(input("Ingrese el rendimiento de la pintura en litros por metro cuadrado: "))
pintura_necesaria = area / rendimiento
print(f"El área de la pared es: {area} metros cuadrados.")
print(f"Para pintar la pared se necesitan {pintura_necesaria} litros de pintura.")