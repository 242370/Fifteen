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
        ax.bar(x + 0.1 + offset, measurement, width, label=attribute)
        multiplier += 1

    ax.set_xlabel('distances')
    ax.set_title(title)
    ax.set_xticks(x + width, distances)
    ax.legend(loc='upper left', ncols=3)
    ax.set_yscale('log')
    # ax.set_ylim(0, 40)

    plt.show()


def draw_general_stats(title):
    x = np.array(["udane", "nieudane"])
    y = np.array([7082, 352])
    plt.bar(x, y, width=0.4)
    plt.title(title)
    plt.show()


def visualise_general_stats(title, data):
    x = np.array(["udane", "nieudane"])
    y = np.array([data[0], data[1]])
    plt.bar(x, y, width=0.4)
    for i in range(len(x)):
        plt.text(i, y[i], y[i])
    plt.title(title)
    plt.show()

def calculate_average(data: list):
    val = 0
    for i in range(len(data)):
        val += data[i]
    return val / len(data)


# def add_stats(file, order_list):
#     with open(file) as f:
#         lines = f.readlines()
#         if int(lines[0]) > -1:
#             order_list.append(np.longdouble(lines[4]))


def get_data():

    # stats_drlu = [[], [], [], [], [], [], []]
    # stats_drul = [[], [], [], [], [], [], []]
    # stats_ludr = [[], [], [], [], [], [], []]
    # stats_lurd = [[], [], [], [], [], [], []]
    # stats_rdlu = [[], [], [], [], [], [], []]
    # stats_rdul = [[], [], [], [], [], [], []]
    # stats_uldr = [[], [], [], [], [], [], []]
    # stats_ulrd = [[], [], [], [], [], [], []]

    # stats_manh = [[], [], [], [], [], [], []]
    # stats_hamm = [[], [], [], [], [], [], []]
    #
    # stats_dfs = [[], [], [], [], [], [], []]
    # stats_bfs = [[], [], [], [], [], [], []]
    # stats_A = [[], [], [], [], [], [], []]

    success = 0
    failure = 0

    for path, currentDirectory, files in os.walk("\\Users\\jkowa\\Desktop\\Studia\\semestr IV\\Sise\\Fifteen"): # przeszukujemy wszystkie pliki w katalogu
        for file in files:
            #porownanie brute-forcow
            # if file.__contains__("bfs") and file.__contains__("stats") and file.__contains__("drlu"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_drlu[i-1])
            # elif file.__contains__("bfs") and file.__contains__("stats") and file.__contains__("drul"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_drul[i-1])
            # elif file.__contains__("dfs") and file.__contains__("stats") and file.__contains__("ludr"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_ludr[i-1])
            # elif file.__contains__("bfs") and file.__contains__("stats") and file.__contains__("lurd"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_lurd[i-1])
            # elif file.__contains__("bfs") and file.__contains__("stats") and file.__contains__("rdlu"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_rdlu[i-1])
            # elif file.__contains__("bfs") and file.__contains__("stats") and file.__contains__("rdul"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_rdul[i-1])
            # elif file.__contains__("bfs") and file.__contains__("stats") and file.__contains__("uldr"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_uldr[i-1])
            # elif file.__contains__("bfs") and file.__contains__("stats") and file.__contains__("ulrd"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_ulrd[i-1])

            # porownanie heurystyk
            # if file.__contains__("hamm") and file.__contains__("stats"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_hamm[i-1])
            # elif file.__contains__("manh") and file.__contains__("stats"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_manh[i-1])

            # porownanie calych algorytmow
            # if file.__contains__("astr") and file.__contains__("stats"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_A[i-1])
            # elif file.__contains__("bfs") and file.__contains__("stats"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_bfs[i - 1])
            # elif file.__contains__("dfs") and file.__contains__("stats"):
            #     for i in range(1, 8):
            #         if file.__contains__("_0" + str(i) + "_"):
            #             add_stats(file, stats_dfs[i - 1])
    # porownanie udanych i nieuanych prob rozwiazan dla kazdego algorytmu
            if file.__contains__("bfs") and file.__contains__("stats"):
                    with open(file) as f:
                        lines = f.readlines()
                        if int(lines[0]) > -1:
                            success += 1
                        else:
                            failure += 1

    # stats = [stats_drlu, stats_drul, stats_ludr, stats_lurd, stats_rdlu, stats_rdul, stats_uldr, stats_ulrd]
    # stats = [stats_hamm, stats_manh]
    # stats = [stats_A, stats_bfs, stats_dfs]
    stats = [success, failure]
    return stats

def main():
    stats = get_data()
    # print(stats[0])
    # average_stats = [[], [], [], [], [], [], [], []]
    # average_stats = [[], []]
    # average_stats = [[], [], []]
    # for i in range(len(stats)): # dla kazdego porzadku przeszukiwania
    #     for j in range(len(stats[i])): # ilosc krokow dla kazdego porzadku przeszukiwan
    #         # print(calculate_average(stats[i][j]))
    #         average_stats[i].append(calculate_average(stats[i][j]))

    # steps = {"drlu": average_stats[0],
    #          "drul": average_stats[1],
    #          "ludr": average_stats[2],
    #          "lurd": average_stats[3],
    #          "rdlu": average_stats[4],
    #          "rdul": average_stats[5],
    #          "uldr": average_stats[6],
    #          "ulrd": average_stats[7]
    #          }

    # steps = {"hamm": average_stats[0],
    #          "manh": average_stats[1]
    #          }

    # steps = {"A*": average_stats[0],
    #          "bfs": average_stats[1],
    #          "dfs": average_stats[2]
    #          }

    # create_histogram("Wszystkie algorytmy - czas trwania procesu obliczeniowego w ms dla wszystkich odleglosci", steps)

    # draw_general_stats("zestawienie udanych i nieudanych prob")
    print(stats[0])
    print(stats[1])
    visualise_general_stats("BFS - zestawienie udanych i nieudanych prob rozwiazania ukladow", stats)


main()




