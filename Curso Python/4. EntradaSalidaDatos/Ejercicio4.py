#Ejercicio 1
'''Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''

vocal = input("Escribir una vocal: ")
letra = input("Escribe aqui tu letra: ")

vocal = (vocal.upper())
letra = (letra.lower())
print("La letra fue: {} \nLa vocal fue: {}".format(letra , vocal))

#Ejercicio 2
'''Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
Te llamas: <nombre>
Tu edad es: <edad>
Eres: <sexo>'''

nombre = input("Escribe aqui tu nombre: ")
edad = int(input("Escribe aqui tu edad: "))
sexo = input("Escribe aqui tu sexo: ")

print("Hola {}, tienes {}, eres {}".format(nombre, edad, sexo))
print("Te llamas: {}\nTu edad es: {}\nEres: {}".format(nombre, edad, sexo))