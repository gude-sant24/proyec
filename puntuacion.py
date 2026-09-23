puntuacio_A = int(input("Ingrese la puntuación A: "))
puntuacio_B = int(input("Ingrese la puntuación B: "))
puntuacio_C = int(input("Ingrese la puntuación C: "))
orden = sorted([puntuacio_A, puntuacio_B, puntuacio_C], reverse=True)
if orden [0] == orden [1]:
    print("hay un empate.")
else :
    print(f"la mayor puntuacion es: {orden[0]}")
