# =============================================================================
# 12. MÓDULOS ESTÁNDAR DE PYTHON
# =============================================================================

print(f"\n=== 12. MÓDULOS ESTÁNDAR DE PYTHON ===")

# Módulo datetime
import datetime
from datetime import date, timedelta

print(f"\n--- Módulo datetime ---")
ahora = datetime.datetime.now()
hoy = date.today()
print(f"Fecha y hora actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Solo fecha: {hoy}")

# timedalta sirve para operaciones con fechas
# Cálculos con fechas
hace_una_semana = hoy - timedelta(days=7)
en_30_dias = hoy + timedelta(days=30)
print(f"Hace una semana: {hace_una_semana}")
print(f"En 30 días: {en_30_dias}")

# Módulo random
import random

print(f"\n--- Módulo random ---")
print(f"Número aleatorio entre 1 y 100: {random.randint(1, 100)}")
print(f"Número flotante aleatorio: {random.random():.3f}")

colores = ["rojo", "azul", "verde", "amarillo", "morado"]
print(f"Color aleatorio: {random.choice(colores)}")

# Mezclar lista
numeros_originales = list(range(1, 11))
numeros_mezclados = numeros_originales.copy()
random.shuffle(numeros_mezclados)
print(f"Números originales: {numeros_originales}")
print(f"Números mezclados: {numeros_mezclados}")

# Muestra aleatoria
muestra = random.sample(range(1, 51), 5)  # 5 números del 1 al 50
print(f"Muestra aleatoria de lotería: {sorted(muestra)}")

# Módulo os
import os

print(f"\n--- Módulo os ---")
print(f"Directorio actual: {os.getcwd()}")
print(f"Sistema operativo: {os.name}") # nt significa Windows, posix para Linux/Mac

# Variables de entorno (simuladas)
print("Variables de entorno importantes:")
env_vars = ["PATH", "HOME", "USER", "PYTHON_PATH"]
for var in env_vars:
    valor = os.environ.get(var, "No definida")
    print(f"  {var}: {valor[:50]}..." if len(str(valor)) > 50 else f"  {var}: {valor}")

# Módulo json
import json

print(f"\n--- Módulo json ---")
# Datos de ejemplo
usuario = {
    "id": 1,
    "nombre": "Juan Pérez",
    "edad": 30,
    "email": "juan@example.com",
    "activo": True,
    "hobbies": ["lectura", "programación", "viajes"],
    "direccion": {
        "calle": "Calle Principal 123",
        "ciudad": "Madrid",
        "codigo_postal": "28001"
    }
}

# Convertir a JSON
json_string = json.dumps(usuario, indent=2, ensure_ascii=False) # ensure_ascii=False para caracteres especiales y dumps para convertir a string
print("Datos convertidos a JSON:")
print(json_string)

# Convertir de vuelta a diccionario
usuario_recuperado = json.loads(json_string) # loads para convertir de string a diccionario
print(f"\nNombre recuperado: {usuario_recuperado['nombre']}")
print(f"Hobbies: {', '.join(usuario_recuperado['hobbies'])}")

# =============================================================================
# 13. ENRUTAMIENTO DE MÓDULOS Y PAQUETES
# =============================================================================

print(f"\n=== 13. ENRUTAMIENTO DE MÓDULOS Y PAQUETES ===")

# Simulación de estructura de paquetes
print(f"\nESTRUCTURA DE PAQUETES SIMULADA")
print("""
mi_proyecto/
│
├── main.py
├── config.py
├── utils/
│   ├── __init__.py
│   ├── matematicas.py
│   ├── texto.py
│   └── archivo.py
├── modelos/
│   ├── __init__.py
│   ├── usuario.py
│   ├── producto.py
│   └── pedido.py
└── servicios/
    ├── __init__.py
    ├── email.py
    ├── pago.py
    └── inventario.py
""")

# --- PAQUETE: utils ---
class UtilsMatematicas:
    @staticmethod
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def fibonacci(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

class UtilsTexto:
    @staticmethod
    def limpiar_texto(texto):
        import re
        # Eliminar caracteres especiales y espacios extra
        texto_limpio = re.sub(r'[^\w\s]', '', texto)
        return ' '.join(texto_limpio.split())
    
    @staticmethod
    def contar_caracteres(texto, incluir_espacios=True):
        if incluir_espacios:
            return len(texto)
        else:
            return len(texto.replace(' ', ''))

# --- PAQUETE: modelos ---
class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.activo = True
        self.fecha_registro = datetime.date.today()
    
    def __str__(self):
        return f"Usuario({self.id}, {self.nombre}, {self.email})"
    
    def desactivar(self):
        self.activo = False
    
    def activar(self):
        self.activo = True

class Producto:
    def __init__(self, id_producto, nombre, precio, stock=0):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        return f"Producto({self.nombre}, ${self.precio}, Stock: {self.stock})"
    
    def agregar_stock(self, cantidad):
        self.stock += cantidad
    
    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

class Pedido:
    contador_pedidos = 0
    
    def __init__(self, usuario, productos):
        Pedido.contador_pedidos += 1
        self.id = Pedido.contador_pedidos
        self.usuario = usuario
        self.productos = productos  # Lista de tuplas (producto, cantidad)
        self.fecha = datetime.date.today()
        self.total = self.calcular_total()
    
    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.productos)
    
    def __str__(self):
        return f"Pedido({self.id}, {self.usuario.nombre}, ${self.total:.2f})"

# --- PAQUETE: servicios ---
class ServicioEmail:
    @staticmethod
    def enviar_confirmacion(usuario, pedido):
        # Simulación de envío de email
        print(f"Email enviado a {usuario.email}")
        print(f"   Asunto: Confirmación de pedido #{pedido.id}")
        print(f"   Total: ${pedido.total:.2f}")
        return True

class ServicioPago:
    @staticmethod
    def procesar_pago(pedido, metodo="tarjeta"):
        # Simulación de procesamiento de pago
        print(f"Procesando pago de ${pedido.total:.2f} con {metodo}")
        # Simular éxito aleatorio
        exito = random.choice([True, True, True, False])  # 75% éxito
        if exito:
            print("   Pago procesado exitosamente")
        else:
            print("   Error en el procesamiento del pago")
        return exito

class ServicioInventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
        self.productos[producto.id] = producto
    
    def buscar_producto(self, id_producto):
        return self.productos.get(id_producto)
    
    def listar_productos_disponibles(self):
        return [p for p in self.productos.values() if p.stock > 0]
    
    def productos_bajo_stock(self, limite=5):
        return [p for p in self.productos.values() if 0 < p.stock <= limite]

# =============================================================================
# DEMOSTRACIÓN DEL SISTEMA COMPLETO
# =============================================================================

print(f"\nDEMOSTRACIÓN DEL SISTEMA DE COMERCIO ELECTRÓNICO")

# Inicializar servicios
inventario = ServicioInventario()

# Crear productos
productos = [
    Producto(1, "Laptop Gaming", 1299.99, 10),
    Producto(2, "Mouse Inalámbrico", 29.99, 50),
    Producto(3, "Teclado Mecánico", 89.99, 25),
    Producto(4, "Monitor 4K", 399.99, 8),
    Producto(5, "Auriculares", 79.99, 3)  # Bajo stock
]

# Agregar productos al inventario
for producto in productos:
    inventario.agregar_producto(producto)

# Crear usuarios
usuarios = [
    Usuario(1, "Ana García", "ana@email.com"),
    Usuario(2, "Carlos López", "carlos@email.com"),
    Usuario(3, "María Rodríguez", "maria@email.com")
]

print("--- INVENTARIO INICIAL ---")
for producto in inventario.productos.values():
    print(f"  {producto}")

print("\n--- PRODUCTOS CON BAJO STOCK ---")
bajo_stock = inventario.productos_bajo_stock()
for producto in bajo_stock:
    print(f"  {producto}")

# Procesar algunos pedidos
print(f"\n--- PROCESAMIENTO DE PEDIDOS ---")

# Pedido 1: Ana compra laptop y mouse
pedido1 = Pedido(usuarios[0], [
    (inventario.buscar_producto(1), 1),  # 1 laptop
    (inventario.buscar_producto(2), 2)   # 2 mouse
])

print(f"Pedido creado: {pedido1}")

# Reducir stock
for producto, cantidad in pedido1.productos:
    if producto.reducir_stock(cantidad):
        print(f"  Stock reducido: {producto.nombre} (-{cantidad})")
    else:
        print(f"  Stock insuficiente: {producto.nombre}")

# Procesar pago y enviar email
if ServicioPago.procesar_pago(pedido1):
    ServicioEmail.enviar_confirmacion(pedido1.usuario, pedido1)

# Pedido 2: Carlos intenta comprar muchos auriculares
print(f"\n--- SEGUNDO PEDIDO ---")
pedido2 = Pedido(usuarios[1], [
    (inventario.buscar_producto(5), 5)   # 5 auriculares (solo hay 3)
])

print(f"Pedido creado: {pedido2}")

# Verificar stock
for producto, cantidad in pedido2.productos:
    if producto.stock < cantidad:
        print(f"  Stock insuficiente: {producto.nombre} "
              f"(Solicitado: {cantidad}, Disponible: {producto.stock})")
    else:
        producto.reducir_stock(cantidad)
        print(f"  Stock reducido: {producto.nombre} (-{cantidad})")