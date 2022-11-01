#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra = input("Introduce una palabra: ")
vocal = ["a","e","i","o","u"]
for n in palabra:
    if n in vocal:
        print("La vocal a se repite",palabra.count("a"), "veces")
        print("La vocal e se repite",palabra.count("e"), "veces")
        print("La vocal i se repite",palabra.count("i"), "veces")
        print("La vocal o se repite",palabra.count("o"), "veces")
        print("La vocal u se repite",palabra.count("u"), "veces")
else: ()