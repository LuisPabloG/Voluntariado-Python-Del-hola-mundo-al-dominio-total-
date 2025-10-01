# *1* Abre un archivo y lo cierra automáticamente al finalizar el bloque
with open ("Archivos txt/Txt_conferencia.txt"):
    print("hola")

# *2* Abre un archivo en modo lectura y lo cierra automáticamente al finalizar el bloque
with open ("Archivos txt/Txt_conferencia.txt",'r'):
    print("hola")
# *3* Abre un archivo en modo lectura y lo cierra automáticamente al finalizar el bloque
with open ("Archivos txt/Txt_conferencia.txt") as archivo:
    print(archivo.read())

# *4* Abre un archivo en modo lectura con codificación UTF-8 y lo cierra automáticamente al finalizar el bloque
with open ("Archivos txt/Txt_conferencia.txt",encoding="UTF-8") as archivo:
    print(archivo.read())
