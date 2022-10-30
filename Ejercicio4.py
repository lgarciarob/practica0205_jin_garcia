#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
nume_loteria = []
for nume_loteria_ganadora in range(6):
    nume_loteria.append(int(input("Introduce el número ganador de la lotería: ")))
nume_loteria.sort()
print("Los numeros ganadores son:", nume_loteria)