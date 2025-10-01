nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

# Para números, ¡recuerda la conversión!
edad_str = input("¿Cuántos años tienes? ")
edad_int = int(edad_str) # Convierte a entero
print(f"¡Qué bien! Ya has vivido {edad_int} años.")

# Para números flotantes
precio_str = input("Introduce un precio: ")
precio_float = float(precio_str)
print(f"El precio es: ${precio_float:.2f}")