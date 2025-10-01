# =============================================================================
# 2. TUPLAS
# =============================================================================

print("\n=== 2. TUPLAS ===")

# Creación de tuplas
tupla_vacia = ()
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mixta = ("Python", 3.11, True, [1, 2, 3])

# ¡CUIDADO! Tupla de un elemento debe llevar una coma al final
tupla_correcta = (42,)  # Con coma
no_es_tupla = (42)      # Sin coma, es solo un int

print(f"Tipo de tupla_correcta: {type(tupla_correcta)}")
print(f"Tipo de no_es_tupla: {type(no_es_tupla)}")

# Acceso y slicing
print(f"Primer elemento: {tupla_numeros[0]}")
print(f"Último elemento: {tupla_numeros[-1]}")
print(f"Slice [1:4]: {tupla_numeros[1:4]}")

# Métodos de tuplas
numeros_repetidos = (1, 2, 2, 3, 2, 4, 2)
print(f"Cantidad de 2's: {numeros_repetidos.count(2)}")
print(f"Índice del primer 3: {numeros_repetidos.index(3)}")

