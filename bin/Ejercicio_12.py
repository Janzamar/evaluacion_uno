#Ejercicio 12
# Encontrar secuencias que contengan un codón de paro

secuencias = input("Dame secuencias separadas por comas, por favor\n").split(", ")

secuencias_paro =[secuencia for secuencia in secuencias if "TAA" in secuencia or "TAG" in secuencia or "TGA" in secuencia]
print(secuencias_paro)