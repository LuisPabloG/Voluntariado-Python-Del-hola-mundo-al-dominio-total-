# =============================================================================
# 4. DICCIONARIOS AVANZADOS
# =============================================================================

print("\n=== 4. DICCIONARIOS AVANZADOS ===")

# Constructor dict()
dict1 = dict()  # Vacío
dict2 = dict(nombre="Juan", edad=30, ciudad="Madrid")
dict3 = dict([("a", 1), ("b", 2), ("c", 3)])
dict4 = dict(zip(["x", "y", "z"], [10, 20, 30]))    # Zip se usa para combinar dos listas

print(f"Dict2: {dict2}")
print(f"Dict3: {dict3}")
print(f"Dict4: {dict4}")

# fromkeys() - Crear diccionario con claves predefinidas
estudiantes = ["Ana", "Bob", "Carlos", "Diana"]
calificaciones = dict.fromkeys(estudiantes, [])  # ¡PELIGRO!
print(f"\nCalificaciones iniciales: {calificaciones}")

# ¡PROBLEMA! Todas las listas son el mismo objeto
calificaciones["Ana"].append(85)
print(f"Después de agregar nota a Ana: {calificaciones}")  # ¡Todas tienen la nota!

# SOLUCIÓN CORRECTA:
calificaciones_correctas = {estudiante: [] for estudiante in estudiantes}
calificaciones_correctas["Ana"].append(85)
calificaciones_correctas["Bob"].append(90)
print(f"Forma correcta: {calificaciones_correctas}")

# Métodos útiles de diccionarios
estudiante = {"nombre": "María", "edad": 22, "carrera": "Ingeniería"}

# get() con valor por defecto
telefono = estudiante.get("telefono", "No disponible")
print(f"\nTeléfono: {telefono}")

# setdefault() - Establece valor si la clave no existe
estudiante.setdefault("universidad", "No especificada")
estudiante.setdefault("edad", 25)  # No cambia porque ya existe
print(f"Estudiante con universidad: {estudiante}")

# update() - Actualizar con otro diccionario
nuevos_datos = {"telefono": "123-456-789", "edad": 23}
estudiante.update(nuevos_datos)
print(f"Estudiante actualizado: {estudiante}")

# Comprensiones de diccionarios
# Crear un diccionario de cuadrados de números del 1 al 5
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"\nCuadrados: {cuadrados}")
