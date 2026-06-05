import matplotlib.pyplot as plt
import random
import sqlite3
def minecraft(efficiency, damage, spechial, filename="sas.png"):
    plt.figure(figsize=(8, 7))
    plt.title('эфективность против мобов')
    plt.xlabel("урон")
    plt.ylabel("способности")
    plt.plot( damage, marker="o", color='r', linestyle='__', label='урон')
    plt.plot( spechial, marker="o", color='b', linestyle='__', label='способности')
    plt.plot( efficiency, marker="o", color='g', linestyle='__', label='эфективность против мобов')
    
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)
    plt.close()
    return filename
degrees_d = [random.randint(10, 25) for _ in range(7)]
degrees_n = [el-random.randint(5, 10) for el in degrees_d]
week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
file_path = minecraft(week, degrees_d, degrees_n)
print(f"График сохранен в файле: {file_path}")
def get_minecraft(efficiency, damage, spechial):
    con = sqlite3.connect('minecraft.db')
    cur = con.cursor()
