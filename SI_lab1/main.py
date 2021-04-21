import sys
import time
import numpy
from chart import create_chart
from operators import test_generic_algorithm, random_method


def print_list(list):
    for i in range(len(list)):
        print(list[i])


if __name__ == '__main__':
    """worst = []
    best = []

    bests_list = []
    worsts_list = []
    best_list_to_plot = []
    worst_list_to_plot = []
    avg_list_to_plot = []

    start = time.time()
    print(start)

    for i in range(10):
        the_best, min_list, max_list, avg_list, count_list = test_generic_algorithm("tournament")
        best.append(min(min_list))
        worst.append(max(max_list))
        bests_list.append(min_list)
        worsts_list.append(max_list)
    for i in range(len(count_list)):
        max_value = 0
        min_value = sys.maxsize
        sum_min_value = 0
        sum_max_value = 0
        for j in range(len(worsts_list)):
            sum_min_value += bests_list[j][i]
            sum_max_value += worsts_list[j][i]
            if min_value > bests_list[j][i]:
                min_value = bests_list[j][i]
        best_list_to_plot.append(min_value)
        worst_list_to_plot.append(sum_max_value / len(worsts_list))
        avg_list_to_plot.append(sum_min_value / len(bests_list))

    create_chart(best_list_to_plot, worst_list_to_plot, avg_list_to_plot, count_list)

    end = time.time()
    print(end)

    print("Min value")
    print(min(best))
    print("Max value")
    print(max(worst))
    print("Avg value")
    print(round(sum(best) / len(best), 2))
    print("Std value")
    print(round(numpy.std(best), 2))

    print("\n")
    print(end - start)"""

    worst = []
    best = []

    bests_list = []
    worsts_list = []
    best_list_to_plot = []
    worst_list_to_plot = []
    avg_list_to_plot = []

    start = time.time()
    print(start)

    for i in range(10):
        the_best, min_list, max_list, avg_list, count_list = random_method()
        best.append(min(min_list))
        worst.append(max(max_list))
        bests_list.append(min_list)
        worsts_list.append(max_list)
    for i in range(len(count_list)):
        max_value = 0
        min_value = sys.maxsize
        sum_min_value = 0
        sum_max_value = 0
        for j in range(len(worsts_list)):
            sum_min_value += bests_list[j][i]
            sum_max_value += worsts_list[j][i]
            if min_value > bests_list[j][i]:
                min_value = bests_list[j][i]
        best_list_to_plot.append(min_value)
        worst_list_to_plot.append(sum_max_value / len(worsts_list))
        avg_list_to_plot.append(sum_min_value / len(bests_list))

    create_chart(best_list_to_plot, worst_list_to_plot, avg_list_to_plot, count_list)

    end = time.time()
    print(end)

    print("Min value")
    print(min(best))
    print("Max value")
    print(max(worst))
    print("Avg value")
    print(round(sum(best) / len(best), 2))
    print("Std value")
    print(round(numpy.std(best), 2))

    print("\n")
    print(end - start)
