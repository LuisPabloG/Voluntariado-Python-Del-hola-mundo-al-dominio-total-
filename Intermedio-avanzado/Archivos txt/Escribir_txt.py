# *1*  Abre un archivo en modo escritura (crea el archivo si no existe) y lo cierra automáticamente al finalizar el bloque
with open ("Archivos txt/Txt_conferencia.txt",'w',encoding="UTF-8") as archivo:
    archivo.write ("Esta es la ultima parte del curos de python")

# *2* Abre un archivo en modo escritura (crea el archivo si no existe) y lo cierra automáticamente al finalizar el bloque
with open ("Archivos txt/Txt_conferencia.txt",'w',encoding="UTF-8") as archivo:
    archivo.writelines ("Esta es la ultima parte del curos de python")

# *3* sobreescribe el archivo con multiples lineas con error 
with open ("Archivos txt/Txt_conferencia.txt",'w',encoding="UTF-8") as archivo:
    archivo.writelines("Aprendiendo a manejar archivos txt en python","Aprendiendo el ultimo bloque de la conferencia")

# *4* sobreescribe el archivo con multiples lineas correctas
with open ("Archivos txt/Txt_conferencia.txt",'w',encoding="UTF-8") as archivo:
    archivo.writelines(["Aprendiendo a manejar archivos txt en python","Aprendiendo el ultimo bloque de la conferencia\n"])

# *5* sobreescribe el archivo con multiples lineas correctas y agrega mas lineas
with open ("Archivos txt/Txt_conferencia.txt",'w',encoding="UTF-8") as archivo:
    archivo.writelines(["Aprendiendo a manejar archivos txt en python","Aprendiendo el ultimo bloque de la conferencia\n"]) 
    archivo.writelines(["Aprendiendo a manejar archivos txt en python","Aprendiendo el ultimo bloque de la conferencia\n"]) 
    
# *6*  agrega mas lineas sin borrar lo que ya habia
with open ("Archivos txt/Txt_conferencia.txt",'a',encoding="UTF-8") as archivo:
    archivo.writelines(["Aprendiendo a manejar archivos txt en python","Aprendiendo el ultimo bloque de la dfafasfasf\n"]) 