'''Ejercicio 1

En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}'''

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

#diccionario = (input("Escriba el país para conocer su capital: "))

if diccionario.capitalize() == "Guatemala":
    print("La capital es: Ciudad de Guatemala")
elif diccionario.capitalize() == "El Salvador":
    print("La capital es: San Salvador")
elif diccionario.capitalize() == "Honduras":
    print("La capital es: Honduras")
else:
    print("Ese país no se encuentra") #Para evitar hacer esto, se hace de la siguiente manera

pais = input("Ingrese el pais para conocer su capital: ")
letra = pais.capitalize() in diccionario

if letra == True:
    print("La capital es: ", diccionario[pais.capitalize()])
else:
    print("El país no se encuentra en el diccinario")

 #O

pais = input("Ingrese el pais para conocer su capital: ")

if pais.capitalize() in diccionario:
    print(diccionario[pais.capitalize()])
else:
    print("El país no se encuentra en el diccinario")

'''Ejercicio 2

Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}'''
diccionario = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

numero = int(input("Escoja el numero del jugador: "))

print("Escogio: ", numero)

if numero in diccionario:
    print("El jugador es: ",diccionario[numero])
else:
    print("Ese numero de jugador no es valido")

