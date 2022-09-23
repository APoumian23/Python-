'''Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
# extraño < -- > tamaño
#desligo < -- > amigo
#riman < -- > cuerpo
#sol < -- > lol
#lo < -- > yo'''

palabra1 = input("Ingresa la primer palabra: ")
palabra2 = input("Ingresa la segunda palabra: " )

if len(palabra1) < 3 or len (palabra2) < 3:
    print("NO rima, porque tienen menos de 3 caracteres")
elif palabra1 [-3: ] == palabra2 [-3: ]:
   print("Las palabras riman ")
elif palabra1[-2: ] == palabra2 [-2: ]:
    print("Las palabras riman un poco ")
else :
   print("Las palabras no riman ")







'''Ejercicio 2

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula'''

candidatoA = "Partido rojo"
candidatoB = "Partido verde"
candidatoC = "Partido azul"

candidato = input("Escoja la letra del candidato aquí (ABC): ")

print(candidato.upper())
if candidato.upper()== "A":
    print("Usted a votado por el partido rojo")
elif candidato.upper() == "B":
    print("Usted a votado por el partido verde")
elif candidato.upper() == "C":
    print("Usted a votado por el partido azul")
else:
    print("Opción Erronea")
