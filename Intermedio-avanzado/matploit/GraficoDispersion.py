import matplotlib.pyplot as plt
horas_estudio = [2, 3, 4, 5, 6, 7, 8, 9]
calificaciones = [60, 65, 70, 72, 75, 80, 85, 90]

plt.scatter(horas_estudio, calificaciones, color="green")
plt.title("Relación entre horas de estudio y calificación")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación (%)")
plt.show()
