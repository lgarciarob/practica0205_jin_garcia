#Escribir un programa que almacene el abecedario en una lista,
# elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
for letra in range(len(abc),1,-1):
    if letra % 3 == 0:
        abc.pop(letra-1)
print(abc)
