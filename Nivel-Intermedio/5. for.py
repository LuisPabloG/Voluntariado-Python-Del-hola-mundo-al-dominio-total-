# =============================================================================
# 5. BUCLE FOR
# =============================================================================

print("\n=== 5. BUCLE FOR ===")

# Iteración básica
frutas = ["manzana", "banana", "naranja", "kiwi"]
print("Frutas disponibles:")
for i, fruta in enumerate(frutas, 1):
    print(f"  {i}. {fruta}")

# Iteración sobre rangos
print("\nTabla del 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Iteración sobre diccionarios
persona = {"nombre": "Carlos", "edad": 28, "trabajo": "Desarrollador"}
print(f"\nInformación de la persona:")
for clave, valor in persona.items():
    print(f"  {clave.capitalize()}: {valor}")

# Múltiples secuencias con zip
nombres = ["Ana", "Bob", "Carlos"]
edades = [25, 30, 35]
ciudades = ["Madrid", "Barcelona", "Valencia"]

print(f"\nInformación completa:")
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"  {nombre}, {edad} años, vive en {ciudad}")

# Bucles anidados - Tabla de multiplicar
# Los for anidados permiten recorrer múltiples dimensiones de datos
print(f"\nTabla de multiplicar (1-5):")
for i in range(1, 6): # Filas 
    for j in range(1, 6):   # Columnas 
        print(f"{i*j:2d}", end=" ") # end=" " evita el salto de línea y pone un espacio
    print()  # Nueva línea
