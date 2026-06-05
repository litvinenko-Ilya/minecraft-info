import matplotlib.pyplot as plt
import random
import sqlite3

def minecraft(efficiency, damage, special, filename="sas.png"):
    plt.figure(figsize=(8, 7))
    plt.title('Эффективность против мобов')
    plt.xlabel("Урон")
    plt.ylabel("Способности")
    
    plt.plot(damage, marker="o", color='r', linestyle='-', label='Урон')  # Используем '-', чтобы показать линию
    plt.plot(special, marker="o", color='b', linestyle='-_ _', label='Способности')
    plt.plot(efficiency, marker="o", color='g', linestyle='--', label='Эффективность против мобов')  # Исправлен стиль линии '--'
    
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)
    plt.close()
    return filename


degrees_d = [random.randint(10, 25) for _ in range(7)]  
degrees_n = [el - random.randint(5, 10) for el in degrees_d]  
week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']  


efficiency = [(d + n)/2 for d, n in zip(degrees_d, degrees_n)]


file_path = minecraft(efficiency, week, degrees_d)

print(f"График сохранён в файле: {file_path}")



def get_minecraft(efficiency, damage, special):
    con = sqlite3.connect('minecraft.db')
    cur = con.cursor()
