# =============================================================================
# 7. FUNCIONES NATIVAS
# =============================================================================

print("\n=== 7. FUNCIONES NATIVAS ===")

# Funciones de transformación
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Números originales: {numeros}")

# map() - Aplicar función a cada elemento
cuadrados = list(map(lambda x: x**2, numeros)) # Elevar al cuadrado cada número 
print(f"Cuadrados: {cuadrados}")

# filter() - Filtrar elementos según condición 
pares = list(filter(lambda x: x % 2 == 0, numeros)) # Números pares 
impares = list(filter(lambda x: x % 2 == 1, numeros)) # Números impares
print(f"Pares: {pares}")
print(f"Impares: {impares}")

# zip() - Combinar iterables
nombres = ["Producto A", "Producto B", "Producto C"]
precios = [25.99, 39.50, 15.75]
productos = list(zip(nombres, precios)) # Lista de tuplas (nombre, precio) 
print(f"\nProductos y precios: {productos}")

# Funciones de agregación
ventas = [1250, 980, 1850, 720, 1340, 2100, 890]
print(f"\nVentas semanales: {ventas}")
print(f"Total de ventas: ${sum(ventas)}")
print(f"Venta máxima: ${max(ventas)}")
print(f"Venta mínima: ${min(ventas)}")
print(f"Promedio: ${sum(ventas) / len(ventas):.2f}")
print(f"Ventas ordenadas: {sorted(ventas, reverse=True)}")

# any() y all()
calificaciones_aprobadas = [85, 90, 78, 92, 88]
calificaciones_mixtas = [85, 45, 78, 92, 60]

print(f"\nTodos aprobaron (>=70): {all(cal >= 70 for cal in calificaciones_aprobadas)}") # all devuelve True si todos cumplen la condición
print(f"Alguien aprobó (>=70): {any(cal >= 70 for cal in calificaciones_mixtas)}") # any devuelve True si al menos uno cumple la condición

# enumerate() - Enumerar elementos con índice 
tareas = ["Comprar", "Estudiar", "Ejercitarse", "Leer"]
print(f"\nLista de tareas:")
for indice, tarea in enumerate(tareas, 1):
    print(f"  {indice}. {tarea}")

# Funciones de conversión
datos_mixtos = ["123", "45.67", "True", "0", "hello"]
print(f"\nConversiones:")
for dato in datos_mixtos:
    try:
        como_int = int(dato)
        print(f"'{dato}' -> int: {como_int}")
    except ValueError:
        try:
            como_float = float(dato)
            print(f"'{dato}' -> float: {como_float}")
        except ValueError:
            print(f"'{dato}' -> no es numérico, bool: {bool(dato)}")