palabra = input("Introduce una palabra: ")
if str(palabra) == str(palabra)[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")