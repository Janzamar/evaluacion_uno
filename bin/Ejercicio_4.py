# Ejercicio 4
# Eliminar adaptadores de secuencias

from pathlib import Path #usamos esta funcion para indicar en dónde está el archivo 4_input_adapters.txt

# especificamos la ruta donde se encuentra el archivo, guardamos en ruta
ruta = Path("\\Users\\asus\\OneDrive\\Documents\\AAAEstudiar LCG\\evaluacion_uno\\data")  # Cambia esto a la ruta correcta

inputfile = ruta / "4_input_adapters.txt"
outputfile = ruta / "4_input_no_adapters.txt"


# Lee el archivo de entrada 4_input_adapters.txt
with open(inputfile, "r") as infile, open(outputfile, "w") as outfile:
    for linea in infile:
        # corte de adaptadores de la secuencia 4_input_adapters.txt. Los adaptadores son los primeros 1-14 caracteres de cada secuencia.
        secuencia_limpia = linea.strip()[14:]
        # salida del file
        outfile.write(f"{secuencia_limpia}\n")
        