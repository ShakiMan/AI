import sys
from copy import copy, deepcopy
from random import randint, uniform
from board.pcb import PCB
from data_loader import ReadData

CROSSOVER_PROBABILITY = 0.4
POPULATION_SIZE = 200
NUMBER_OF_GENERATIONS = 100
COMPLETE_MUTATION_PROBABILITY = 0.01


def tournament_operator(pcb_population, percentage_of_population=0.1):
    n = len(pcb_population) * percentage_of_population
    if n == 0:
        n = 1

    selected_individuals = {}
    while len(selected_individuals) < n:
        random_individual = randint(0, len(pcb_population) - 1)
        selected_individuals[random_individual] = pcb_population[random_individual].quality

    best_quality = sys.maxsize
    best_quality_index = 0
    for index, quality in selected_individuals.items():
        if quality < best_quality:
            best_quality = quality
            best_quality_index = index
    return pcb_population[best_quality_index]


def roulette_operator(pcb_population, percentage_of_population=0.1):
    selected_individuals = {}
    total_quality = 0
    for pcb in pcb_population:
        total_quality += pcb.quality
    total_reverse_quality = 0
    for pcb in pcb_population:
        total_reverse_quality += total_quality - pcb.quality
    while len(selected_individuals) < len(pcb_population) * percentage_of_population:
        rand = randint(1, int(total_reverse_quality))
        total_searched_quality = 0
        for i in range(len(pcb_population)):
            total_searched_quality += total_quality - pcb_population[i].quality
            if total_searched_quality > rand:
                selected_individuals[i] = pcb_population[i].quality
                break
    return pcb_population[choose_the_best(selected_individuals)]


def choose_the_best(pcb_list):
    the_best_score = sys.maxsize
    the_best_score_index = 0
    for index, score in pcb_list.items():
        if score < the_best_score:
            the_best_score = score
            the_best_score_index = index
    return the_best_score_index


def crossover_operator(first_parent, second_parent):
    new_pcb = PCB(copy(first_parent.points_list), first_parent.width, first_parent.height)
    number_of_path = len(first_parent.paths_list)
    rand = randint(0, number_of_path - 1)
    for i in range(0, rand):
        new_pcb.paths_list.append(deepcopy(first_parent.paths_list[i]))
    for i in range(rand, number_of_path):
        new_pcb.paths_list.append(deepcopy(second_parent.paths_list[i]))
    return new_pcb


def mutation_operator(pcb, chance_for_mutation=0.95):
    chance = uniform(0, 1)
    if chance < chance_for_mutation:
        if chance < COMPLETE_MUTATION_PROBABILITY:
            pcb.create_random_solution()
            return
        rand = randint(0, len(pcb.paths_list) - 1)
        pcb.change_path_solution(pcb.paths_list[rand])


def test_generic_algorithm(type_of_selection="roulette"):
    worst_list = []
    avg_list = []
    best_list = []
    count_list = []
    t = 0
    list_of_populations = [initialize_start_population()]
    evaluate_population(list_of_populations[t])
    last_best_quality = sys.maxsize
    len_list_of_populations = len(list_of_populations[0])

    population_count = 0
    while population_count <= NUMBER_OF_GENERATIONS + 1:
        list_of_populations.append([])
        while len(list_of_populations[t + 1]) != len_list_of_populations:
            if type_of_selection == "tournament":
                p1 = tournament_operator(list_of_populations[t])
                p2 = tournament_operator(list_of_populations[t])
            elif type_of_selection == "roulette":
                p1 = roulette_operator(list_of_populations[t])
                p2 = roulette_operator(list_of_populations[t])

            if uniform(0, 1) < CROSSOVER_PROBABILITY:
                o1 = crossover_operator(p1, p2)
            else:
                o1 = deepcopy(p1)
            evaluate_pcb(o1)
            mutation_operator(o1, 0.1)
            evaluate_pcb(o1)
            list_of_populations[t + 1].append(o1)
            if last_best_quality > o1.quality:
                last_best_quality = o1.quality
                the_best_solution = o1


        list_of_populations.pop(t)

        best = sys.maxsize
        for individual in list_of_populations[0]:
            if individual.quality < best:
                best = individual.quality
        best_list.append(best)

        worst = 0
        for individual in list_of_populations[0]:
            if individual.quality > worst:
                worst = individual.quality
        worst_list.append(worst)

        sum = 0
        for individual in list_of_populations[0]:
            sum += individual.quality
        avg = sum / len(list_of_populations[0])
        avg_list.append(avg)
        count_list.append(population_count)
        population_count += 1
    return the_best_solution, best_list, worst_list, avg_list, count_list


def random_method():
    worst_list = []
    avg_list = []
    best_list = []
    count_list = []

    last_best_quality = sys.maxsize
    population_count = 0
    while population_count <= NUMBER_OF_GENERATIONS + 1:
        o1 = initialize_start_population()
        len_list_of_populations = len(o1)
        for i in range(len_list_of_populations):
            evaluate_pcb(o1[i])
            if last_best_quality > o1[i].quality:
                last_best_quality = o1[i].quality
                the_best_solution = o1[i]

        best = sys.maxsize
        for individual in o1:
            if individual.quality < best:
                best = individual.quality
        best_list.append(best)

        worst = 0
        for individual in o1:
            if individual.quality > worst:
                worst = individual.quality
        worst_list.append(worst)

        sum = 0
        for individual in o1:
            sum += individual.quality
        avg = sum / len(o1)
        avg_list.append(avg)
        count_list.append(population_count)
        population_count += 1
    return the_best_solution, best_list, worst_list, avg_list, count_list







def initialize_start_population():
    reader = ReadData("TestData\zad2.txt")
    width, height, points_list = reader.get_data()
    population_list = []
    for i in range(POPULATION_SIZE):
        pcb = PCB(points_list, width, height)
        pcb.assign_points()
        pcb.create_random_solution()
        pcb.repair_paths()
        population_list.append(pcb)
    return population_list


def evaluate_population(population_list):
    for pcb in population_list:
        pcb.create_clean_board()
        pcb.evaluate_board()


def evaluate_pcb(pcb):
    pcb.create_clean_board()
    pcb.evaluate_board()
