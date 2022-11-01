#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista
# , pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
asignatura = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nota_modulo = []
for modulo in asignatura:
    print("Introduce tu nota del modulo",modulo)
    nota = float(input())
if nota >= 5:
    asignatura.remove(nota_modulo.index(nota))
else:
    nota_modulo.append(nota)
