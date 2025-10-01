import pandas as pd 

df = pd.read_csv("Archivos csv/archivocsv.csv",names=["carnet","nombre","edad"])

edad_ordenada = df.sort_values("edad", ascending=False)
print(edad_ordenada)
