valor_cuenta = int(input("Ingrese el valor de la cuenta: "))
propina = int(input("Ingrese el porcentaje de propina que desea dejar (sin el símbolo %): "))
personas = int(input("Ingrese el número de personas que van a pagar la cuenta: "))
if personas <= 0:
    print("El número de personas debe ser mayor que cero.")
else :
    total_propina = valor_cuenta * (propina / 100)
    total_cuenta = valor_cuenta + total_propina
    pago_por_persona = total_cuenta / personas
    print(f"El total de la propina es: {total_propina}")
    print(f"El total de la cuenta con propina es: {total_cuenta}")
    print(f"Cada persona debe pagar: {pago_por_persona}")
    