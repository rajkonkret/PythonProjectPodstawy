import matplotlib.pyplot as plt

labels = ["Jabłka", "Banany", "Winoggrono", "Pomarańcza"]
sizes = [30, 25, 20, 45]
colors = ["red", 'blue', 'green', 'yellow']

plt.pie(
    sizes, labels=labels, colors=colors, autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    explode=(0.1, 0, 0, 0)
)

plt.axis('equal')

plt.show()
