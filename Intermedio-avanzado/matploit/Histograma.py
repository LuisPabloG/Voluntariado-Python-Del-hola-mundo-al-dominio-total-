import matplotlib.pyplot as plt
horas_sueno = [6, 7, 8, 5, 6, 9, 7, 8, 6, 7, 5, 8, 9, 6, 7]

plt.hist(horas_sueno, bins=5, color="purple", edgecolor="black")
plt.title("Distribución de horas de sueño")
plt.xlabel("Horas de sueño")
plt.ylabel("Frecuencia")
plt.show()
