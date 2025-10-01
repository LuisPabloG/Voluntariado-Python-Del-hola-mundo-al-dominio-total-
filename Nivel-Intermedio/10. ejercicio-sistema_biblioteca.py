# =============================================================================
# 10. EJERCICIO INTEGRADOR: SISTEMA DE BIBLIOTECA
# =============================================================================

print("\n=== 10. EJERCICIO INTEGRADOR: SISTEMA DE BIBLIOTECA ===")

# Base de datos de libros (lista de diccionarios)
biblioteca = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "García Márquez", 
     "genero": "Realismo mágico", "año": 1967, "disponible": True},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", 
     "genero": "Distopía", "año": 1949, "disponible": True},
    {"id": 3, "titulo": "El Quijote", "autor": "Cervantes", 
     "genero": "Clásico", "año": 1605, "disponible": False},
    {"id": 4, "titulo": "Harry Potter", "autor": "J.K. Rowling", 
     "genero": "Fantasía", "año": 1997, "disponible": True},
    {"id": 5, "titulo": "Orgullo y prejuicio", "autor": "Jane Austen", 
     "genero": "Romance", "año": 1813, "disponible": True}
]

def mostrar_biblioteca(libros):
    """Muestra todos los libros de la biblioteca"""
    print("\n📚 CATÁLOGO DE LA BIBLIOTECA")
    print("-" * 50)
    for libro in libros:
        estado = "✅ Disponible" if libro["disponible"] else "❌ Prestado"
        print(f"ID: {libro['id']:2d} | {libro['titulo']:<20} | "
              f"{libro['autor']:<15} | {libro['año']} | {estado}")

def buscar_por_genero(libros, genero_buscado):
    """Busca libros por género usando filter y lambda"""
    return list(filter(lambda libro: genero_buscado.lower() in libro["genero"].lower(), 
                      libros))

def buscar_por_año(libros, año_inicio, año_fin):
    """Busca libros en un rango de años"""
    return list(filter(lambda libro: año_inicio <= libro["año"] <= año_fin, 
                      libros))

def libros_disponibles(libros):
    """Retorna solo los libros disponibles"""
    return list(filter(lambda libro: libro["disponible"], libros))

def ordenar_libros(libros, criterio="titulo"):
    """Ordena libros por diferentes criterios"""
    criterios = {
        "titulo": lambda x: x["titulo"],
        "autor": lambda x: x["autor"],
        "año": lambda x: x["año"],
        "id": lambda x: x["id"]
    }
    
    if criterio in criterios:
        return sorted(libros, key=criterios[criterio])
    else:
        return libros

def estadisticas_biblioteca(libros):
    """Calcula estadísticas de la biblioteca"""
    total_libros = len(libros)
    disponibles = sum(1 for libro in libros if libro["disponible"])
    prestados = total_libros - disponibles
    
    # Obtener géneros únicos
    generos = set(libro["genero"] for libro in libros)
    
    # Libro más antiguo y más reciente
    mas_antiguo = min(libros, key=lambda x: x["año"])
    mas_reciente = max(libros, key=lambda x: x["año"])
    
    # Promedio de año de publicación
    promedio_año = sum(libro["año"] for libro in libros) / total_libros
    
    return {
        "total": total_libros,
        "disponibles": disponibles,
        "prestados": prestados,
        "generos": generos,
        "mas_antiguo": mas_antiguo,
        "mas_reciente": mas_reciente,
        "promedio_año": promedio_año
    }

# Demostración del sistema
mostrar_biblioteca(biblioteca)

# Búsquedas
print(f"\n🔍 BÚSQUEDAS")
fantasticos = buscar_por_genero(biblioteca, "fantasía")
print(f"Libros de fantasía: {[libro['titulo'] for libro in fantasticos]}")

clasicos = buscar_por_año(biblioteca, 1800, 1900)
print(f"Libros del siglo XIX: {[libro['titulo'] for libro in clasicos]}")

disponibles = libros_disponibles(biblioteca)
print(f"Libros disponibles: {len(disponibles)} de {len(biblioteca)}")

# Ordenamiento
print(f"\n📋 ORDENAMIENTO")
por_año = ordenar_libros(biblioteca, "año")
print("Libros ordenados por año:")
for libro in por_año:
    print(f"  {libro['año']}: {libro['titulo']}")

# Estadísticas
print(f"\n📊 ESTADÍSTICAS")
stats = estadisticas_biblioteca(biblioteca)
print(f"Total de libros: {stats['total']}")
print(f"Disponibles: {stats['disponibles']}")
print(f"Prestados: {stats['prestados']}")
print(f"Géneros disponibles: {', '.join(stats['generos'])}")
print(f"Libro más antiguo: {stats['mas_antiguo']['titulo']} ({stats['mas_antiguo']['año']})")
print(f"Libro más reciente: {stats['mas_reciente']['titulo']} ({stats['mas_reciente']['año']})")
print(f"Promedio año publicación: {stats['promedio_año']:.0f}")

# Usando comprensiones para análisis adicional
print(f"\n🎯 ANÁLISIS CON COMPRENSIONES")

# Títulos de libros disponibles en mayúsculas
titulos_disponibles = [libro["titulo"].upper() for libro in biblioteca if libro["disponible"]]
print(f"Títulos disponibles: {titulos_disponibles}")

# Diccionario de géneros y cantidad
contador_generos = {}
for libro in biblioteca:
    genero = libro["genero"]
    contador_generos[genero] = contador_generos.get(genero, 0) + 1
print(f"Libros por género: {contador_generos}")

# Autores únicos
autores_unicos = set(libro["autor"] for libro in biblioteca)
print(f"Autores únicos: {autores_unicos}")

print("\n" + "="*80)