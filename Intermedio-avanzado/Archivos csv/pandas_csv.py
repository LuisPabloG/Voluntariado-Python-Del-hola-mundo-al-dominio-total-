# *1* Leer un archivo csv con pandas
import pandas as pd 

archivo = pd.read_csv("Archivos csv/archivocsv.csv")
print(archivo)
# *2*  Leer un archivo csv con pandas y mostrar una columna
import pandas as pd 

df = pd.read_csv("Archivos csv/archivocsv.csv")
print(df["nombre"])
# *3* Leer un archivo csv con pandas y asignar nombres a las columnas
import pandas as pd 

df = pd.read_csv("Archivos csv/archivocsv.csv",names=["carnet","nombre","edad"])
print(df)
#*4* eslaising
data = "123450"
print(data[2:5])

# *5*  Leer un archivo csv con pandas, asignar nombres a las columnas y ordenar por edad
df = pd.read_csv("Archivos csv/archivocsv.csv",names=["carnet","nombre","edad"])

edad_ordenada = df.sort_values("edad")
print(edad_ordenada)