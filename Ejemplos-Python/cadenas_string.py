
datos = "nombre,edad,ciudad"
lista_datos = datos.split(",")  # ['nombre', 'edad', 'ciudad']
nueva_cadena = "-".join(lista_datos) # nombre-edad-ciudad
print(lista_datos)
print(nueva_cadena)


email = " test@example.com "
print(email.strip()) # test@example.com
print(email.strip().endswith(".com")) # True

