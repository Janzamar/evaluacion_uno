#Ejercicio 13
# contar cuantos nt hay en cada secuencia 

secuencias = input("Dame secuencias de DNA separadas por comas, por favor\n").split(", ")

conteo = [[f"A: {secuencia.count('A') }", f"T: {secuencia.count('T') }", f"C: {secuencia.count('C') }", f"G {secuencia.count('G')}" ] for secuencia in secuencias]
print(conteo) 