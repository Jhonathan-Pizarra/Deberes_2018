print("*** OPERADORES LÓGICOS ***")
print("AND")
usuario1 = "Crhistian"
usuario2 = "Cristhiam"
usuario3 = "Crhistian"

if usuario1 and usuario2 == usuario3:
    print("Ambos se llaman Crhistian")

else:
    print("El nombre de uno de ellos no es Crhistian")

print("")
print("OR")
usuario4 = "Jhon"
usuario5 = "Jhonathan"
usuario6 = "Jhon"

if usuario4 or usuario5 == usuario6:
    print("Al menos uno de los dos se llama Jhon")

else:
    print("Ninguno de los dos se llama Jhon")

print("")
print("NOT")
estaLloviendo = True

if not estaLloviendo: #Si no es verdad que está lloviendo
    print("Vamos afuera")

else:
    print("Nos quedamos en casa!") #Porque está lloviendo es: True