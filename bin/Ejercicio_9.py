# Ejericio 9
# transformar secuencias de DNA a RNA

secuencias = input("Dame secuencias separadas por comas, por favor\n").split(", ")

secuencias_rna =[secuencia.replace ("T","U") for secuencia in secuencias]

print(secuencias_rna)
