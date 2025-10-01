import csv

with open ("Archivos csv/archivocsv.csv") as archivo_csv:
    reader = csv.reader(archivo_csv)
    for fila in reader:
        print(fila)