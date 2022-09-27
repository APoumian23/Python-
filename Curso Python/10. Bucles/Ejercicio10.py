'''Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero'''

numero = int(input("Escribe un numero para mostrar la tabla de multiplicar: "))
i = 0
multi = 0

while i <=10:
    multi = numero * i
    print("{}x{}={}".format(numero, i, multi))
    i += 1


'''Ejercicio 2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''

edad = int(input("Escribe tu edad: "))
print("Tu edad es: {}".format(edad))
i = 1


while i !=edad:
    print("Has cumplido: {} anios".format(i))
    i += 1

while i <= edad:
    print("Has cumplido: {} anios".format(i))
    i += 1

