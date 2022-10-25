#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura,
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura>
# es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
asignatura = list(["Matemáticas", "Física", "Química", "Historia", "Lengua"])
nota_modulo = []
for modulo in asignatura:
    print("Introduce tu nota del modulo",modulo)
    nota_modulo.append(input())
for cali in range(len(asignatura)):
    print(asignatura[cali],"=", nota_modulo[cali])