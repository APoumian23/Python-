cadena = "Estoy mostrando los metodos booleanos para las strings"
cadena2 = "ESTOY MOSTRANDO LOS METODOS BOOLEANOS PARA LAS STRINGS"
cadena3 = "estoy mostrando los metodos booleanos para las strings"

print (cadena.startswith("E")) #Para checar si el parametro es correcto, si se hace con otra letra dará falso o si se hace siendo mayuscula o minuscula 
print (cadena.endswith("s"))

print(cadena2.isupper()) #Para verificar que todo este en mayusculas
print(cadena.isupper()) #Da falso porque no todo esta en mayuscula
print(cadena.islower()) #Para verificar que todo este en minusculas 
print(cadena3.islower())