#Calcular el Iva de un valor ingresado por teclado

print("Ingresa el monto a calcular: ")
costo = int(input())
iva = 12
calculo = costo*iva /100

total = costo + calculo


print(f"Costo:  {costo}")
print(f"Porcentaje-IVA:  {iva}"+"%")
print(f"Calculo-IVA:  ${calculo}")
print(f"Total:   {total}")

