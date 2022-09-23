lista = ['Python', 24, "Rene", "alexander", 12]

print(lista)
lista[3] = "Alexander"
print(lista)
print(lista[3])

lista.pop() #Elimina el ultimo elemento de la lista
print(lista)
lista.pop()
print(lista)

lista.remove(12) #Elimina el elemento que se escoge
print(lista)
lista.remove("Python")
print(lista)