# =============================================================================
# 9. FUNCIONES LAMBDA
# =============================================================================

print("\n=== 9. FUNCIONES LAMBDA ===")

# Funciones lambda básicas
cuadrado = lambda x: x ** 2
suma = lambda a, b: a + b
es_par = lambda x: x % 2 == 0

print(f"Cuadrado de 5: {cuadrado(5)}")
print(f"Suma de 3 + 7: {suma(3, 7)}")
print(f"¿8 es par?: {es_par(8)}")

# Lambda con condicionales 
mayor = lambda a, b: a if a > b else b
signo = lambda x: "positivo" if x > 0 else "negativo" if x < 0 else "cero"

print(f"Mayor entre 10 y 7: {mayor(10, 7)}")
print(f"Signo de -5: {signo(-5)}")

# Uso con funciones nativas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Con map() - Elevar al cubo cada número
cubos = list(map(lambda x: x**3, numeros))
print(f"\nCubos: {cubos[:5]}...")  # Solo primeros 5

# Con filter() - Filtrar múltiplos de 3
multiplos_de_3 = list(filter(lambda x: x % 3 == 0, numeros))
print(f"Múltiplos de 3: {multiplos_de_3}")

# Con sorted() - Ordenar lista de tuplas
estudiantes = [("Ana", 85), ("Bob", 92), ("Carlos", 78), ("Diana", 96)]

por_nombre = sorted(estudiantes, key=lambda x: x[0])
por_nota = sorted(estudiantes, key=lambda x: x[1], reverse=True)

print(f"\nEstudiantes por nombre: {por_nombre}")
print(f"Estudiantes por nota: {por_nota}")

# Lambda en diccionarios
operaciones = {
    "suma": lambda a, b: a + b,
    "resta": lambda a, b: a - b,
    "multiplicacion": lambda a, b: a * b,
    "division": lambda a, b: a / b if b != 0 else "Error: División por cero"
}

print(f"\nCalculadora con lambdas:")
print(f"10 + 5 = {operaciones['suma'](10, 5)}")
print(f"10 - 5 = {operaciones['resta'](10, 5)}")
print(f"10 * 5 = {operaciones['multiplicacion'](10, 5)}")
print(f"10 / 5 = {operaciones['division'](10, 5)}")
print(f"10 / 0 = {operaciones['division'](10, 0)}")

# Lambda con max() y min() en listas de diccionarios
productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 50},
    {"nombre": "Teclado", "precio": 75, "stock": 20},
    {"nombre": "Monitor", "precio": 300, "stock": 8}
]

mas_caro = max(productos, key=lambda p: p["precio"])
menos_stock = min(productos, key=lambda p: p["stock"])
nombre_mas_largo = max(productos, key=lambda p: len(p["nombre"]))

print(f"\nAnálisis de productos:")
print(f"Más caro: {mas_caro['nombre']} (${mas_caro['precio']})")
print(f"Menos stock: {menos_stock['nombre']} ({menos_stock['stock']} unidades)")
print(f"Nombre más largo: {nombre_mas_largo['nombre']}")