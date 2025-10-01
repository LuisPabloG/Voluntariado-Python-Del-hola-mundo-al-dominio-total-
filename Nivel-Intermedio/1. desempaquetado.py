print("=== 1. DESEMPAQUETADO ===")

# Ejemplo 1: Desempaquetado básico
coordenadas = (10, 20)
x, y = coordenadas
print(f"Coordenada X: {x}, Coordenada Y: {y}")

# Ejemplo 2: Desempaquetado con asterisco
# El asterisco permite capturar múltiples valores en una lista
numeros = [1, 2, 3, 4, 5, 6, 7]
primero, segundo, *resto, ultimo = numeros
print(f"Primero: {primero}")
print(f"Segundo: {segundo}")
print(f"Resto: {resto}")
print(f"Último: {ultimo}")

# Ejemplo 3: Intercambio de variables
# Sin variable temporal
a, b = 10, 20
print(f"Antes - a: {a}, b: {b}")
a, b = b, a
print(f"Después - a: {a}, b: {b}")

# Ejemplo 4: Desempaquetado en función
def mostrar_datos(nombre, edad, ciudad, *hobbies):
    print(f"\n--- Información Personal ---")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Hobbies: {', '.join(hobbies)}")

persona = ("Ana García", 25, "Madrid", "Leer", "Viajar", "Programar")
mostrar_datos(*persona) # asterisco para desempaquetar la tupla