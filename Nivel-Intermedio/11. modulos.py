# =============================================================================
# 11. MÓDULOS - CREACIÓN Y USO
# =============================================================================

print("=== 11. MÓDULOS ===")

# Simulación de módulos (en la práctica, estos estarían en archivos separados)

# --- MÓDULO: matematicas.py ---
def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(base, exponente):
    """Calcula la potencia de un número"""
    return base ** exponente

def factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Constante del módulo
PI = 3.14159265359

# --- MÓDULO: utilidades_texto.py ---
def contar_palabras(texto):
    """Cuenta las palabras en un texto"""
    return len(texto.split())

def invertir_texto(texto):
    """Invierte el orden de los caracteres"""
    return texto[::-1]

def es_palindromo(texto):
    """Verifica si un texto es un palíndromo"""
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

def capitalizar_palabras(texto):
    """Capitaliza cada palabra del texto"""
    return " ".join(palabra.capitalize() for palabra in texto.split())

def extraer_numeros(texto):
    """Extrae todos los números de un texto"""
    import re
    return [int(num) for num in re.findall(r'\d+', texto)]

# --- MÓDULO: estadisticas.py ---
def media(numeros):
    """Calcula la media aritmética"""
    return sum(numeros) / len(numeros) if numeros else 0

def mediana(numeros):
    """Calcula la mediana"""
    if not numeros:
        return 0
    
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    
    if n % 2 == 0:
        return (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        return numeros_ordenados[n//2]

def moda(numeros):
    """Encuentra la moda (valor más frecuente)"""
    if not numeros:
        return None
    
    frecuencias = {}
    for num in numeros:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    
    max_frecuencia = max(frecuencias.values())
    modas = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
    
    return modas[0] if len(modas) == 1 else modas

def desviacion_estandar(numeros):
    """Calcula la desviación estándar"""
    if len(numeros) < 2:
        return 0
    
    promedio = media(numeros)
    varianza = sum((x - promedio) ** 2 for x in numeros) / (len(numeros) - 1)
    return varianza ** 0.5

# =============================================================================
# DEMOSTRACIÓN DE USO DE MÓDULOS
# =============================================================================

print("\nUSO DE MÓDULOS PERSONALIZADOS")

# Uso del módulo matemáticas
print(f"\n--- Módulo Matemáticas ---")
print(f"5 + 3 = {sumar(5, 3)}")
print(f"10 - 4 = {restar(10, 4)}")
print(f"6 * 7 = {multiplicar(6, 7)}")
print(f"15 / 3 = {dividir(15, 3)}")
print(f"2^8 = {potencia(2, 8)}")
print(f"5! = {factorial(5)}")
print(f"Valor de π: {PI}")

# Manejo de errores
try:
    print(f"10 / 0 = {dividir(10, 0)}")
except ValueError as e:
    print(f"Error: {e}")

# Uso del módulo utilidades de texto
print(f"\n--- Módulo Utilidades de Texto ---")
texto_ejemplo = "Hola mundo desde Python"
print(f"Texto original: '{texto_ejemplo}'")
print(f"Número de palabras: {contar_palabras(texto_ejemplo)}")
print(f"Texto invertido: '{invertir_texto(texto_ejemplo)}'")
print(f"Palabras capitalizadas: '{capitalizar_palabras(texto_ejemplo)}'")

# Extraer números de texto
texto_con_numeros = "En 2024 vendimos 150 productos por un total de 25000 dólares"
numeros_encontrados = extraer_numeros(texto_con_numeros)
print(f"Números encontrados en '{texto_con_numeros}': {numeros_encontrados}")

# Uso del módulo estadísticas
print(f"\n--- Módulo Estadísticas ---")
datos_ventas = [120, 150, 130, 200, 180, 160, 140, 170, 190, 150]
print(f"Datos de ventas: {datos_ventas}")
print(f"Media: {media(datos_ventas):.2f}")
print(f"Mediana: {mediana(datos_ventas):.2f}")
print(f"Moda: {moda(datos_ventas)}")
print(f"Desviación estándar: {desviacion_estandar(datos_ventas):.2f}")