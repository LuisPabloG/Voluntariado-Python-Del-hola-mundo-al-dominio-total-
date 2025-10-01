# =============================================================================
# 6. BUCLE WHILE
# =============================================================================

print("\n=== 6. BUCLE WHILE ===")

# Ejemplo básico: Cuenta regresiva
print("Cuenta regresiva:")
contador = 5
while contador > 0:
    print(f"  {contador}...")
    contador -= 1
print("  ¡Despegue! 🚀")

# Validación de entrada (simulado)
print(f"\n--- Simulación de validación ---")
intentos = 0
numero_secreto = 7
adivinanza = 0

# Simular intentos de adivinanza
numeros_intentos = [5, 3, 7]  # Simulamos entrada del usuario
for intento in numeros_intentos:
    intentos += 1
    print(f"Intento {intentos}: {intento}")
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("Muy bajo")
    else:
        print("Muy alto")

# Bucle infinito controlado (simulado)
print(f"\n--- Simulación de menú ---")
comandos = ["help", "status", "exit"]  # Simulamos entrada
for comando in comandos:
    print(f"Comando ingresado: {comando}")
    if comando == "help":
        print("  Comandos disponibles: help, status, exit")
    elif comando == "status":
        print("  Sistema funcionando correctamente")
    elif comando == "exit":
        print("  Saliendo del sistema...")
        break
    else:
        print("  Comando no reconocido")

# Control de flujo: break, continue, else
print(f"\nBuscar número primo:")
numeros_test = [10, 11, 12, 13, 14, 15]

for num in numeros_test:
    if num < 2:
        continue # Saltar números menores que 2
    
    for i in range(2, int(num**0.5) + 1): # Solo verificar hasta la raíz cuadrada de num
        if num % i == 0: # Encontrado un divisor
            print(f"{num} no es primo (divisible por {i})")
            break
    else:
        print(f"{num} ES PRIMO")