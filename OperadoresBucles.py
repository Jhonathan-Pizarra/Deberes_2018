print("*** OPERADORES DE INCREMENTO, DECREMENTO Y ASGINACIÓN ***")
print("SUMAR:")
numero = 0
for i in range(5):
    numero = numero+1
    #O también: numero += 1 (Operador de incremento)
    print(numero)

print("")
print("MULTIPLICAR:")
numero2 = 2
for i in range(5):
    numero2 *= 2
    print(numero2)

print("")
print("ELEVAR A:")
numero3 = 2
for i in range(3):
    numero3 **= 3 #2= 2*2*2
                    #8 = 8*8*8
                        #512 = 512*512*512
    print(numero3)

print("")
print("RESIDUO DE:")
numero4 = 16
for i in range(5):
    numero4 %= 2 #Solo está asignando el valor del modulo de la division para 2 en cada iteración...
    print(numero4)

print("")
print("DIVIDIR N PARTES ENTERAS:")
numero5 = 32
for i in range(5):
    numero5 //= 2 #Va a quitar 2 en cada iteración
    print(numero5)

print("")
print("DIVIDIR N PARTES FLOTANTES")
numero6 = 32
for i in range(5):
    numero6 /= 2
    print(numero6)

print("")
print("RESTAR:")
numero7 = 5
for i in range(5):
    numero7 -= 1 #Aqui se hace 4
    print(numero7) #Aqui imprime por primera vez...

print("")
print("ASIGNACIÓN")
numero8 = 78;
numero9 = numero8
print(numero9)
#La comparación sería ==