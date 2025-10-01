# *1* Abrir y leer un archivo csv
with open ("Archivos csv/archivocsv.csv") as archivo:
    print("archivo leido correctamente")

# *2* Abrir y leer un archivo csv
with open ("Archivos csv/archivocsv.csv") as archivo_csv:
    print(archivo_csv.read())

# *3*  Leer un archivo csv con el modulo csv
import csv
with open ("Archivos csv/archivocsv.csv") as archivo_csv:
    print(csv.reader(archivo_csv))  # Imprime el objeto reader
    
# *4* Recorrer un archivo csv con el modulo csv

with open ("Archivos csv/archivocsv.csv") as archivo_csv:
    reader = csv.reader(archivo_csv)
    for fila in reader:
        print(fila)
        
        