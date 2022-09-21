cadena = "Te quiero solo como amigo"

print(len(cadena))
print(cadena[0:2]) #Sacar primeros dos caracteres
print(cadena[22 : 25]) #Sacar ultimos 3 caracteres
print(cadena[-3 : ]) #Sacar ultimos 3 caracteres 

print(cadena[: : 2]) #Truco para sacar cada dos de copia
print(cadena[: : -1]) #Para imprimir de uno en uno a la inversa
print(cadena + cadena[: : -1]) #Imprime ambas cadenas pero la ultima se imprime invertida 

#Metodo de Replace
palabra = "Separado"

print(palabra.replace("", ",")) #De esta forma se reemplaza entre cada letra con una coma

print(palabra.replace("o" , "a")) #Así se reemplaza la e por a, haciendo la palabra como Separada

palabra = "eparado"
print(palabra)

reemplazar = palabra.replace("" , ",")
print("S" , reemplazar)