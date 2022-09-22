nombre = input("Pon tu nombre aqui: ")
edad = int(input("Pon tu edad aqui: "))

if nombre  == "Alex":
    if edad >= 18:
        print("Eres Alex y eres mayor de edad")
    else:
        print("Eres Alex pero no eres mayor de edad")
else:
    print("Tu NO eres Alex")