#Escribir un programa que almacene en una lista los números del 1 al 10
# y los muestre por pantalla en orden inverso separados por comas.
numero = []
for list in range(10):
    numero.append(int(input("Introduce un número: ")))
numero.reverse()
print(numero)