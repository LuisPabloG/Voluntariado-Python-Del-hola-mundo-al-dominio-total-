import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Frecuencia cardiaca
dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
frecuencia = [72, 75, 70, 80, 78, 74, 76]
axs[0].plot(dias, frecuencia, marker="o", color="blue")
axs[0].set_title("Frecuencia Cardiaca")

# Calorías
calorias = [2200, 2100, 2500, 2300, 2000, 2800, 2600]
axs[1].bar(dias, calorias, color="orange")
axs[1].set_title("Calorías Consumidas")

# Sueño
horas_sueno = [6, 7, 8, 5, 6, 9, 7, 8, 6, 7, 5, 8, 9, 6, 7]
axs[2].hist(horas_sueno, bins=5, color="purple", edgecolor="black")
axs[2].set_title("Horas de Sueño")

plt.tight_layout()
plt.show()
