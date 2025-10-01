import matplotlib.pyplot as plt
dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
calorias = [2200, 2100, 2500, 2300, 2000, 2800, 2600]

plt.bar(dias, calorias, color="orange")
plt.title("Consumo calórico semanal")
plt.xlabel("Días")
plt.ylabel("Calorías")
plt.show()
