'''Ejercicio 1
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal'''

letra = input("Escribe la letra aqui: ")

if letra == "a":
    print("Es vocal")
elif letra == "e":
    print("Es vocal")
elif letra == "i":
    print("Es vocal")
elif letra == "o":
    print("Es vocal")
elif letra == "u":
    print("Es vocal")
else: 
    print("Esta no es una vocal")

if letra in ("aeiou"):
    print("Es una vocal")
else:
    print("Esta no es una vocal")


'''Ejercicio 2
Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).'''

numero = int(input("Ingresa el numero: "))

if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: ".format(numero), numero * -1)


#print(abs(10)) Sirve para sacar el valor absoluto de cualquier numero

numero = int(input("Ingresa el numero: "))

if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: ".format(numero), abs(numero))