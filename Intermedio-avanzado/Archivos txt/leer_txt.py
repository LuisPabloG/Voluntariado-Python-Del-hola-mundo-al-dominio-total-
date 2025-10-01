# *1*Leer un archivo con error
open("texto_conferencia.txt")

# *2*Leer un archivo con direccion
open("Archivos txt/Txt_conferencia.txt")

# *3*Guardar en una variable e imprimir
archivo = open("Archivos txt/Txt_conferencia.txt")
print(archivo)

# *3*Leer el contenido del archivo
archivo = open("Archivos txt/Txt_conferencia.txt")
print(archivo.read())

# *4* Leer el contenido con acentos
archivo = open("Archivos txt/Txt_conferencia.txt",encoding="utf-8")
print(archivo.read())

# *5*  Guardar en una variable e imprimir
archivo = open("Archivos txt/Txt_conferencia.txt",encoding="utf-8")
contenido = archivo.read()
print(contenido)

# *6* leer lineas de archivo erroreo
archivo = open("Archivos txt/Txt_conferencia.txt",encoding="utf-8")
contenido = archivo.read()
contenido = archivo.readlines()
print(contenido)

# *7* leer lineas de archivo correcto
archivo = open("Archivos txt/Txt_conferencia.txt",encoding="utf-8")
contenido = archivo.readlines()
print(contenido)

# *8* Leer readline por linea
archivo = open("Archivos txt/Txt_conferencia.txt",encoding="utf-8")
linea = archivo.readline()
print(linea)

# *9* close
archivo = open("Archivos txt/Txt_conferencia.txt",encoding="utf-8")
linea = archivo.readline()
archivo.close()
print(linea)

# *9* close
archivo = open("Archivos txt/Txt_conferencia.txt",encoding="utf-8")
linea = archivo.readline()
archivo.close()
print(archivo.read())

# *10* close y error
archivo = open("Archivos txt/Txt_conferencia.txt",encoding="utf-8")
linea = archivo.readline()
archivo.close()
print(archivo.read())


