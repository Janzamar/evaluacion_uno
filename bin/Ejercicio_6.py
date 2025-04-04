# Ejercicio 6
# contar lineas del formato

from pathlib import Path #usamos esta funcion para indicar en dónde está el archivo 4_input_adapters.txt

# especificamos la ruta donde se encuentra el archivo, guardamos en ruta
ruta = Path("\\Users\\asus\\OneDrive\\Documents\\AAAEstudiar LCG\\evaluacion_uno\\results")  

inputfile = ruta / "dna_sequences.fa"

with open(inputfile, "r") as infile:
    lineas = infile.readlines() #con readline vaciamos todo el archivo 
    lineas_filtradas = [linea for linea in lineas if linea.startswith(">")] # se guardan las lineas del archivo en un indice de una lista
    print(f"Total de secuencias: {len(lineas_filtradas)}") #len nos ayuda a contar el numero de secuencias del file
