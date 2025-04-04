#Ejercicio 11
# Invertir secuencias de DNA

secuencias = input ("Dame secuencias de DNA separadas por comas\n").split(", ")

secuencias_invertidas = [secuencia.strip()[::-1] for secuencia in secuencias]
print(secuencias_invertidas)