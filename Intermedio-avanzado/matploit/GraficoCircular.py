import matplotlib.pyplot as plt
actividades = ["Estudio", "Trabajo", "Ejercicio", "Ocio", "Sueño"]
tiempos = [4, 8, 1, 3, 8]

plt.pie(tiempos, labels=actividades, autopct="%1.1f%%", startangle=90)
plt.title("Distribución del tiempo diario")
plt.show()
