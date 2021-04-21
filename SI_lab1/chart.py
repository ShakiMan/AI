import matplotlib.pyplot as plt


def create_chart(best_list, worst_list, avg_list, count_list):
    plt.plot(count_list, best_list, label="best")
    plt.plot(count_list, worst_list, label="worst")
    plt.plot(count_list, avg_list, label="avg")
    plt.legend()
    plt.show()
