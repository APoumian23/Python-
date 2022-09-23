'''Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]'''

lista = [20, 50, "Curso", 'Python', 3.14]
print("Estos son los valores actuales de la lista, ", lista)

primerdato = input("Ingrese su primer dato: ")
segundodato = input("Ingrese su segundo dato: ")

print(lista)
lista[0] = primerdato
lista[1] = segundodato
print("El nuevo valor de la lista es: {}".format(lista))



'''Ejercicio 2

Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos'''

'''lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print(len(lista))


print(lista)'''