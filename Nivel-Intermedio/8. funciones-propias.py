# =============================================================================
# 8. CREAR FUNCIONES PROPIAS
# =============================================================================

print("\n=== 8. FUNCIONES PROPIAS ===")

def saludar_personalizado(nombre, saludo="Hola", emoji="👋"):
    """Función que crea un saludo personalizado"""
    return f"{saludo} {nombre}! {emoji}"

# Diferentes formas de llamar la función
print(saludar_personalizado("Ana"))
print(saludar_personalizado("Bob", "Buenos días"))
print(saludar_personalizado("Carlos", emoji="🎉"))
print(saludar_personalizado("Diana", "Bienvenida", "🌟"))

# Función con *args
# *args permite pasar una cantidad variable de argumentos posicionales
def calcular_promedio(*numeros):
    """Calcula el promedio de cualquier cantidad de números"""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

print(f"\nPromedios:")
print(f"Promedio de 5, 7, 3: {calcular_promedio(5, 7, 3)}")
print(f"Promedio de 10, 8, 9, 7, 6: {calcular_promedio(10, 8, 9, 7, 6)}")

# Función con **kwargs
# **kwargs permite pasar una cantidad variable de argumentos nombrados
def crear_perfil(**datos):
    """Crea un perfil de usuario con información variable"""
    perfil = {"creado": True}
    for clave, valor in datos.items():
        perfil[clave] = valor
    return perfil

perfil_basico = crear_perfil(nombre="Juan", edad=25)
perfil_completo = crear_perfil(nombre="María", edad=30, 
                              ciudad="Barcelona", trabajo="Ingeniera")

print(f"\nPerfil básico: {perfil_basico}")
print(f"Perfil completo: {perfil_completo}")

# Función con retorno múltiple
def analizar_numeros(lista_numeros):
    """Analiza una lista de números y retorna estadísticas"""
    if not lista_numeros:
        return None, None, None, None
    
    total = sum(lista_numeros)
    promedio = total / len(lista_numeros)
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    
    return total, promedio, minimo, maximo

datos_ventas = [1200, 850, 1500, 950, 1100, 1350]
total, prom, min_val, max_val = analizar_numeros(datos_ventas)

print(f"\nAnálisis de ventas {datos_ventas}:")
print(f"Total: ${total}")
print(f"Promedio: ${prom:.2f}")
print(f"Mínimo: ${min_val}")
print(f"Máximo: ${max_val}")


# Variables globales vs locales
contador_global = 0

def incrementar_contador():
    global contador_global
    contador_global += 1
    return contador_global

def crear_contador_local():
    contador_local = 0
    def incrementar():
        nonlocal contador_local
        contador_local += 1
        return contador_local
    return incrementar

print(f"\n--- Contadores ---")
print(f"Contador global inicial: {contador_global}")
print(f"Después de incrementar: {incrementar_contador()}")
print(f"Después de incrementar: {incrementar_contador()}")

mi_contador = crear_contador_local()
print(f"Contador local: {mi_contador()}")
print(f"Contador local: {mi_contador()}")