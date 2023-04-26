import os
import numpy as np
import matplotlib.pyplot as plt


distances = ("1", "2", "3", "4", "5", "6", "7")

def create_histogram(title, data):
    x = np.arange(len(distances))
    width = 0.1
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in data.items():
        offset = width * multiplier
        ax.bar(x - 0.2 + offset, measurement, width, label=attribute)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('number of steps')
    ax.set_xlabel('distances')
    ax.set_title(title)
    ax.set_xticks(x + width, distances)
    ax.legend(loc='upper right', ncols=3)
    ax.set_ylim(0, 30)

    plt.show()


def calculate_average(data: list):
    val = 0
    for i in range(len(data)):
        val += data[i]
    return val / len(data)


def add_stats(file, order_list):
    with open(file) as f:
        lines = f.readlines()
        order_list.append(int(lines[0]))


def get_data():

    stats_drlu = [[], [], [], [], [], [], []]
    stats_drul = [[], [], [], [], [], [], []]
    stats_ludr = [[], [], [], [], [], [], []]
    stats_lurd = [[], [], [], [], [], [], []]
    stats_rdlu = [[], [], [], [], [], [], []]
    stats_rdul = [[], [], [], [], [], [], []]
    stats_uldr = [[], [], [], [], [], [], []]
    stats_ulrd = [[], [], [], [], [], [], []]

    for path, currentDirectory, files in os.walk("\\Users\\jkowa\\Desktop\\Studia\\semestr IV\\Sise\\Fifteen"): # przeszukujemy wszystkie pliki w katalogu
        for file in files:
            if file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("drlu"):
                for i in range(1, 8):
                    if file.__contains__("_0" + str(i) + "_"):
                        add_stats(file, stats_drlu[i-1])
            elif file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("drul"):
                for i in range(1, 8):
                    if file.__contains__("_0" + str(i) + "_"):
                        add_stats(file, stats_drul[i-1])
            elif file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("ludr"):
                for i in range(1, 8):
                    if file.__contains__("_0" + str(i) + "_"):
                        add_stats(file, stats_ludr[i-1])
            elif file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("lurd"):
                for i in range(1, 8):
                    if file.__contains__("_0" + str(i) + "_"):
                        add_stats(file, stats_lurd[i-1])
            elif file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("rdlu"):
                for i in range(1, 8):
                    if file.__contains__("_0" + str(i) + "_"):
                        add_stats(file, stats_rdlu[i-1])
            elif file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("rdul"):
                for i in range(1, 8):
                    if file.__contains__("_0" + str(i) + "_"):
                        add_stats(file, stats_rdul[i-1])
            elif file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("uldr"):
                for i in range(1, 8):
                    if file.__contains__("_0" + str(i) + "_"):
                        add_stats(file, stats_uldr[i-1])
            elif file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("ulrd"):
                for i in range(1, 8):
                    if file.__contains__("_0" + str(i) + "_"):
                        add_stats(file, stats_ulrd[i-1])
    stats = [stats_drlu, stats_drul, stats_ludr, stats_lurd, stats_rdlu, stats_rdul, stats_uldr, stats_ulrd]
    return stats

def main():
    stats = get_data()
    print(stats)
    average_stats = [[], [], [], [], [], [], [], []]
    for i in range(len(stats)): # dla kazdego porzadku przeszukiwania
        for j in range(len(stats[i])): # ilosc krokow dla kazdego porzadku przeszukiwan
            print(calculate_average(stats[i][j]))
            average_stats[i].append(calculate_average(stats[i][j]))

    steps = {"drlu": average_stats[0],
             "drul": average_stats[1],
             "ludr": average_stats[2],
             "lurd": average_stats[3],
             "rdlu": average_stats[4],
             "rdul": average_stats[5],
             "uldr": average_stats[6],
             "ulrd": average_stats[7]
             }
    create_histogram("dlugosc rozwiazania dla wszystkich porzadkow przeszukiwan i odleglosci", steps)
    visited_states = {}
    processed_states = {}
    max_depths = {}
    durations = {}


main()




