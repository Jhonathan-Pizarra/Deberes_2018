#Escribir un programa en Python que me pida por teclado el nombre de 2 personas, y sus edades y determinar cuál de ellos es el mayor
print("¿Cómo se llama el usuario: [1]?")
usuario1 = input()
print("¿Qué edad tiene "+ usuario1+"?")
edad1 = int(input())

print("")

print("¿Cómo se llama el usuario: [2]?")
usuario2 = input()
print("¿Qué edad tiene "+ usuario2+"?")
edad2 = int(input())


if edad1 > edad2:
    print(usuario1+" es mayor.")

elif edad1 < edad2: #else if
    print(usuario2 + " es mayor.")

else:
    print("Las edades de "+usuario1 + " y "+ usuario2+ " son iguales")
