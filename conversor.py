temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
redondeo = round(temperatura_fahrenheit, 2)
print(f"La temperatura en grados Fahrenheit es: {redondeo}")