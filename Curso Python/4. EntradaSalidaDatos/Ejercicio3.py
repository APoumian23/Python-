from math import sqrt
a = int(input("Ingresa el valor de a:"))
b = int(input("Ingresa el valor de b:"))
c = int(input("Ingresa el valor de c:"))
x1 = 0
x2 = 0

if((b**2)-(4*a*c)) < 0:
    print("No se puede realizar porque no se puede sacar raiz de numero negativo")
else: 
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
    print("La solucion es: \nx1=",x1, "\nx2=",x2)


p1 = 8
p2 = 9
p3 = 10
EP = 9
EF = 10


PP = (p1+p2+p3)/3
PROM = ((PP + 2*EP + 3*EF)/6)

print(PP)
print(PROM)

practica1 = float(input("Ingrese el valor de la practica1: "))
practica2 = float(input("Ingrese el valor de la practica2: "))
practica3 = float(input("Ingrese el valor de la practica3: "))
ExamenParcial = float(input("Ingrese el valor del ExamenParcial: "))
ExamenFinal = float(input("Ingrese el valor del ExamenFinal: "))

PromedioPractica = (practica1+practica2+practica3)/3
PromedioFinal = ((PromedioPractica) + (2* ExamenParcial) + (3 * ExamenFinal))/6

print("El promedio de practica del estudiante es de: \n",
 PromedioPractica, "\n Y el promedio Final es de:\n", PromedioFinal)

 #\n es para que el dato aparezca abajo y no aun lado