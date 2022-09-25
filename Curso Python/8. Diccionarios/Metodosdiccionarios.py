diccionario = {1 : 2 , 2 : 3 , 3 : 4}
diccionario2 = {4 : 5 , 5 : 6 , 6 : 7}

print(diccionario)
print(diccionario.keys())
print(diccionario.values())

diccionario.pop(1) #Elimina una llave y valor especifico
print(diccionario)

diccionario.clear() #Limpia todo el diccionario
print(diccionario)

print(diccionario.get(2)) #Trae un valor exacto 

diccionario.setdefault(4 , 5) #Incorpora un nuevo valor
print(diccionario)

diccionario.update(diccionario2) #Se combina ambos diccionarios para unirlos y actualiza
print(diccionario)

diccionario.copy()
print(diccionario)
