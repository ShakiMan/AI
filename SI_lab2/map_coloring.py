import time
from typing import List, Dict

from constraint import Constraint, V, D
from constraint_satisfaction_problem import ConstraintSatisfactionProblem


class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, country1: str, country2: str):
        super().__init__([country1, country2])
        self.country1: str = country1
        self.country2: str = country2

    def satisfied(self, assigment: Dict[str, str]) -> bool:
        if self.country1 not in assigment or self.country2 not in assigment:
            return True
        return assigment[self.country1] != assigment[self.country2]

    def get_x_y(self):
        return self.country1, self.country2


def create_map_coloring_csp(variable_h, domain_h):
    variables = [
        "RPA",
        "Lesotho",
        "Suazi",
        "Mozambik",
        "Namibia",
        "Botswana",
        "Zimbabwe",
        "Angola",
        "Zambia",
        "Malawi",
        "Tanzania",
        "Burundi",
        "Rwanda",
        "DRK",
        "Kongo",
        "Gabon",
        "Gwinea Równikowa",
        "Uganda",
        "Kenia",
        "Somalia",
        "Etiopia",
        "Dżibuti",
        "Erytrea",
        "Sudan Południowy",
        "Sudan",
        "Republika Środkowoafrykańska",
        "Czad",
        "Kamerun",
        "Nigeria",
        "Niger",
        "Benin",
        "Togo",
        "Ghana",
        "Burkina Faso",
        "WKS"
    ]

    domains = {}
    for variable in variables:
        domains[variable] = ["green", "blue", "red", "yellow"]

    csp = ConstraintSatisfactionProblem(variables, domains, variable_h, domain_h)

    csp.add_constraint(MapColoringConstraint("RPA", "Lesotho"))
    csp.add_constraint(MapColoringConstraint("RPA", "Suazi"))
    csp.add_constraint(MapColoringConstraint("RPA", "Mozambik"))
    csp.add_constraint(MapColoringConstraint("RPA", "Namibia"))
    csp.add_constraint(MapColoringConstraint("RPA", "Botswana"))
    csp.add_constraint(MapColoringConstraint("RPA", "Zimbabwe"))
    csp.add_constraint(MapColoringConstraint("Suazi", "Mozambik"))
    csp.add_constraint(MapColoringConstraint("Namibia", "Botswana"))
    csp.add_constraint(MapColoringConstraint("Namibia", "Angola"))
    csp.add_constraint(MapColoringConstraint("Namibia", "Zambia"))
    csp.add_constraint(MapColoringConstraint("Mozambik", "Zimbabwe"))
    csp.add_constraint(MapColoringConstraint("Mozambik", "Zambia"))
    csp.add_constraint(MapColoringConstraint("Mozambik", "Malawi"))
    csp.add_constraint(MapColoringConstraint("Botswana", "Zambia"))
    csp.add_constraint(MapColoringConstraint("Botswana", "Zimbabwe"))
    csp.add_constraint(MapColoringConstraint("Zimbabwe", "Zambia"))
    csp.add_constraint(MapColoringConstraint("Angola", "Zambia"))
    csp.add_constraint(MapColoringConstraint("Zambia", "Malawi"))
    csp.add_constraint(MapColoringConstraint("Angola", "DRK"))
    csp.add_constraint(MapColoringConstraint("Zambia", "DRK"))
    csp.add_constraint(MapColoringConstraint("Zambia", "Tanzania"))
    csp.add_constraint(MapColoringConstraint("Malawi", "Tanzania"))
    csp.add_constraint(MapColoringConstraint("Mozambik", "Tanzania"))
    csp.add_constraint(MapColoringConstraint("DRK", "Tanzania"))
    csp.add_constraint(MapColoringConstraint("Burundi", "Rwanda"))
    csp.add_constraint(MapColoringConstraint("DRK", "Burundi"))
    csp.add_constraint(MapColoringConstraint("DRK", "Rwanda"))
    csp.add_constraint(MapColoringConstraint("Tanzania", "Burundi"))
    csp.add_constraint(MapColoringConstraint("Tanzania", "Rwanda"))
    csp.add_constraint(MapColoringConstraint("Rwanda", "Uganda"))
    csp.add_constraint(MapColoringConstraint("Kongo", "DRK"))
    csp.add_constraint(MapColoringConstraint("Kongo", "Gabon"))
    csp.add_constraint(MapColoringConstraint("Gabon", "Gwinea Równikowa"))
    csp.add_constraint(MapColoringConstraint("DRK", "Uganda"))
    csp.add_constraint(MapColoringConstraint("Tanzania", "Uganda"))
    csp.add_constraint(MapColoringConstraint("Tanzania", "Kenia"))
    csp.add_constraint(MapColoringConstraint("Uganda", "Kenia"))
    csp.add_constraint(MapColoringConstraint("Kenia", "Somalia"))
    csp.add_constraint(MapColoringConstraint("Somalia", "Etiopia"))
    csp.add_constraint(MapColoringConstraint("Somalia", "Dżibuti"))
    csp.add_constraint(MapColoringConstraint("Kenia", "Etiopia"))
    csp.add_constraint(MapColoringConstraint("Kenia", "Sudan Południowy"))
    csp.add_constraint(MapColoringConstraint("Uganda", "Sudan Południowy"))
    csp.add_constraint(MapColoringConstraint("DRK", "Sudan Południowy"))
    csp.add_constraint(MapColoringConstraint("Etiopia", "Dżibuti"))
    csp.add_constraint(MapColoringConstraint("Etiopia", "Erytrea"))
    csp.add_constraint(MapColoringConstraint("Dżibuti", "Erytrea"))
    csp.add_constraint(MapColoringConstraint("Etiopia", "Sudan Południowy"))
    csp.add_constraint(MapColoringConstraint("Etiopia", "Sudan"))
    csp.add_constraint(MapColoringConstraint("Sudan Południowy", "Sudan"))
    csp.add_constraint(MapColoringConstraint("Erytrea", "Sudan"))
    csp.add_constraint(MapColoringConstraint("DRK", "Republika Środkowoafrykańska"))
    csp.add_constraint(MapColoringConstraint("Kongo", "Republika Środkowoafrykańska"))
    csp.add_constraint(MapColoringConstraint("Kongo", "Kamerun"))
    csp.add_constraint(MapColoringConstraint("Gabon", "Kamerun"))
    csp.add_constraint(MapColoringConstraint("Gwinea Równikowa", "Kamerun"))
    csp.add_constraint(MapColoringConstraint("Sudan Południowy", "Republika Środkowoafrykańska"))
    csp.add_constraint(MapColoringConstraint("Sudan", "Republika Środkowoafrykańska"))
    csp.add_constraint(MapColoringConstraint("Sudan", "Czad"))
    csp.add_constraint(MapColoringConstraint("Republika Środkowoafrykańska", "Czad"))
    csp.add_constraint(MapColoringConstraint("Republika Środkowoafrykańska", "Kamerun"))
    csp.add_constraint(MapColoringConstraint("Kamerun", "Czad"))
    csp.add_constraint(MapColoringConstraint("Czad", "Niger"))
    csp.add_constraint(MapColoringConstraint("Czad", "Nigeria"))
    csp.add_constraint(MapColoringConstraint("Kamerun", "Nigeria"))
    csp.add_constraint(MapColoringConstraint("Nigeria", "Niger"))
    csp.add_constraint(MapColoringConstraint("Nigeria", "Benin"))
    csp.add_constraint(MapColoringConstraint("Niger", "Benin"))
    csp.add_constraint(MapColoringConstraint("Niger", "Burkina Faso"))
    csp.add_constraint(MapColoringConstraint("Benin", "Burkina Faso"))
    csp.add_constraint(MapColoringConstraint("Benin", "Togo"))
    csp.add_constraint(MapColoringConstraint("Togo", "Burkina Faso"))
    csp.add_constraint(MapColoringConstraint("Togo", "Ghana"))
    csp.add_constraint(MapColoringConstraint("Burkina Faso", "Ghana"))
    csp.add_constraint(MapColoringConstraint("Burkina Faso", "WKS"))
    csp.add_constraint(MapColoringConstraint("Ghana", "WKS"))


    return csp


"""def print_solution(color):
    for s in solution:
        if solution[s] == color:
            print(s, solution[s])"""


def test(variable, domain):
    print("Configuration", variable, "-", domain)
    loops_amount = 200
    sum = 0

    print("Backtracking: ")
    start_time = time.time_ns()
    for i in range(loops_amount):
        csp = create_map_coloring_csp(variable, domain)
        solution1 = csp.backtracking_search()
        sum += csp.visited_nodes
    end_time = time.time_ns()
    time_difference = end_time - start_time
    time_difference = time_difference / loops_amount
    avg_nodes = sum / loops_amount

    print("time avg: ", time_difference)
    print("avg nodes: ", avg_nodes)

    sum = 0
    print("\nForward: ")
    start_time = time.time_ns()
    for i in range(loops_amount):
        csp2 = create_map_coloring_csp(variable, domain)
        solution2 = csp2.forward_checking()
        sum += csp2.visited_nodes
    end_time = time.time_ns()
    time_difference = end_time - start_time
    time_difference = time_difference / loops_amount
    avg_nodes = sum / loops_amount

    print("time avg: ", time_difference)
    print("avg nodes: ", avg_nodes)
    print("\n\n")


if __name__ == "__main__":
    # test("mostConstraints", "random")
    test("firstUnassigned", "leastUsed")
    test("leastConstraints", "leastUsed")
    test("mostConstraints", "leastUsed")
    # test("firstUnassigned", "mostUsed")
    test("mostConstraints", "mostUsed")
    # test("leastConstraints", "mostUsed")
