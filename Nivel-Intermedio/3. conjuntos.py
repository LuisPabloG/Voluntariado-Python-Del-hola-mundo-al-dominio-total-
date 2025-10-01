# =============================================================================
# 3. CONJUNTOS (SETS)
# =============================================================================

print("\n=== 3. CONJUNTOS (SETS) ===")

# Creación de conjuntos
conjunto_vacio = set()
frutas = {"manzana", "banana", "naranja", "manzana"}  # Duplicado se elimina
print(f"Frutas: {frutas}")

# Crear set desde lista con duplicados
numeros_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 5]
numeros_unicos = set(numeros_con_duplicados)
print(f"Números únicos: {numeros_unicos}")

# Operaciones básicas
frutas.add("kiwi")
frutas.update(["uva", "pera", "mango"])
print(f"Después de agregar: {frutas}")

frutas.discard("banana")  # No error si no existe
print(f"Después de eliminar banana: {frutas}")

# Operaciones matemáticas de conjuntos
lenguajes_juan = {"Python", "JavaScript", "Java", "C++"}
lenguajes_ana = {"Python", "C#", "Java", "Go"}

print(f"\nLenguajes Juan: {lenguajes_juan}")
print(f"Lenguajes Ana: {lenguajes_ana}")

# Unión (ambos saben)
todos_lenguajes = lenguajes_juan | lenguajes_ana
print(f"Todos los lenguajes: {todos_lenguajes}")

# Intersección (ambos saben)
lenguajes_comunes = lenguajes_juan & lenguajes_ana
print(f"Lenguajes en común: {lenguajes_comunes}")

# Diferencia (solo Juan sabe)
solo_juan = lenguajes_juan - lenguajes_ana
print(f"Solo Juan sabe: {solo_juan}")

# Diferencia simétrica (uno u otro, pero no ambos)
diferentes = lenguajes_juan ^ lenguajes_ana
print(f"Lenguajes diferentes: {diferentes}")

# Verificación de subconjuntos
basicos = {"Python", "JavaScript"}
print(f"¿{basicos} es subconjunto de Juan?: {basicos.issubset(lenguajes_juan)}")