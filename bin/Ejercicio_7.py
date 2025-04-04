#Ejercicio 7
# Extraer los primeros tres nucleotidos de cada secuencia

secuencias = input("Dame secuencias separadas por comas, por favor\n").split(", ")

codones_de_inicio = [secuencia[:3] for secuencia in secuencias] # los corchetes significan lista
print(codones_de_inicio)