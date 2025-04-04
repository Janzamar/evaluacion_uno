# Ejercicio 5.
#Convertir tsv a fasta

from pathlib import Path #usamos esta funcion para indicar en dónde está el archivo 4_input_adapters.txt

# especificamos la ruta donde se encuentra el archivo, guardamos en ruta
ruta = Path("\\Users\\asus\\OneDrive\\Documents\\AAAEstudiar LCG\\evaluacion_uno\\data")  # Esta es la ruta donde está el archivo


inputfile = ruta / "dna_sequence.txt"
outputfile = ruta / "dna_sequences.fa"

#abrimos el input file
with open(inputfile,"r") as infile, open(outputfile,"w") as outfile:
    for linea in infile:
        id, seq = linea.strip().split("\t") 
        # usamos split para dividir la cadena en subcadenas usando el \t como nuestro separador de columnas
        # usamos id y seq para identificar lo que está haciendo la función de mejor forma
        outfile.write(f">{id}\n{seq.upper()}\n")
