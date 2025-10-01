import matplotlib.pyplot as plt

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
frecuencia = [72, 75, 70, 80, 78, 74, 76]

plt.plot(dias, frecuencia, marker="o", linestyle="-", color="blue", label="Frecuencia cardiaca")
plt.title("Frecuencia Cardiaca Semanal")
plt.xlabel("Días")
plt.ylabel("Latidos por minuto")
plt.legend()
plt.grid(True)
plt.show()

