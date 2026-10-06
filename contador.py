frase = input("ingrese una frase: ")
contador_vocales = 0
contador_consonantes = 0
contador_espacios = 0
contador_numeros = 0
for letra in frase:
    minuscula = letra.lower()
    if minuscula == "a" or minuscula == "e" or minuscula == "i" or minuscula == "o" or minuscula == "u":
        contador_vocales +=1
    elif minuscula == " ":
        contador_espacios +=1
    elif minuscula.isalpha():
        contador_consonantes +=1
    elif minuscula.isdigit():
        contador_numeros +=1
print("la frase tiene", contador_vocales, "vocales")
print("la frase tiene", contador_consonantes, "consonantes")
print("la frase tiene", contador_espacios, "espacios")
print("la frase tiene", contador_numeros, "numeros")
