from typing import Dict

from constraint import Constraint, V, D
from constraint_satisfaction_problem import ConstraintSatisfactionProblem
from house import House


class ZebraPuzzleConstraint(Constraint[str, str]):
    def __init__(self, first, second, are_neighbours=False, neighbour=None):
        super().__init__([first, second])
        self.first = first
        self.second = second
        self.are_neighbours = are_neighbours
        self.neighbour = neighbour


    def satisfied(self, assigment: Dict[str, House]) -> bool:
        if self.are_neighbours and self.first in assigment and self.second in assigment:
            if self.neighbour is None:
                if abs(assigment[self.first].id - assigment[self.second].id) != 1:
                    return False
            elif self.neighbour:
                if assigment[self.first].id - assigment[self.second].id != 1:
                    return False
            else:
                if assigment[self.first].id - assigment[self.second].id != 1:
                    return False

        for a in assigment:
            for s in assigment:
                if s != a:
                    if assigment[s] == assigment[a]:
                        return False

        if self.first not in assigment or self.second not in assigment:
            return True

        if not self.are_neighbours:
            return assigment[self.first] == assigment[self.second]

        return True


def create_zebra_puzzle_csp():
    nationalities = ["Niemiec", "Norweg", "Szwed", "Anglik", "Duńczyk"]
    colors = ["Niebieski", "Zielony", "Czerwony", "Żółty", "Biały"]
    drinks = ["Mleko", "Piwo", "Woda", "Kawa", "Herbata"]
    tobaccos = ["Fajka", "Cygaro", "Papierosy light", "Papierosy bez filtra", "Mentolowe"]
    animals = ["Psy", "Konie", "Koty", "Ptaki", "Rybki"]

    variables = nationalities + colors + drinks + tobaccos + animals

    first_house = House(1)
    second_house = House(2)
    third_house = House(3)
    fourth_house = House(4)
    fifth_house = House(5)

    houses = [House(1), House(2), House(3), House(4), House(5)]
    domains = {}
    for variable in variables:
        domains[variable] = houses

    csp = ConstraintSatisfactionProblem(variables, domains)

    # known dependencies
    domains[nationalities[0]] = [houses[0]] # rule 1
    domains[drinks[4]] = [houses[2]] # rule 8
    domains[colors[3]] = [houses[1]] # rule

    #dependencies about the same house
    csp.add_constraint(ZebraPuzzleConstraint(nationalities[3], colors[2]))
    csp.add_constraint(ZebraPuzzleConstraint(drinks[4], nationalities[4]))
    csp.add_constraint(ZebraPuzzleConstraint(tobaccos[1], colors[3]))
    csp.add_constraint(ZebraPuzzleConstraint(nationalities[0], tobaccos[0]))
    csp.add_constraint(ZebraPuzzleConstraint(tobaccos[3], animals[3]))
    csp.add_constraint(ZebraPuzzleConstraint(nationalities[2], animals[0]))
    csp.add_constraint(ZebraPuzzleConstraint(drinks[3], colors[1]))
    csp.add_constraint(ZebraPuzzleConstraint(tobaccos[4], drinks[1]))

    csp.add_constraint(ZebraPuzzleConstraint(colors[1], colors[4], are_neighbours=True, neighbour=True))
    csp.add_constraint(ZebraPuzzleConstraint(tobaccos[2], animals[2], are_neighbours=True))
    csp.add_constraint(ZebraPuzzleConstraint(tobaccos[2], drinks[2], are_neighbours=True))
    csp.add_constraint(ZebraPuzzleConstraint(animals[1], colors[3], are_neighbours=True))

    return csp

if __name__ == '__main__':
    csp = create_zebra_puzzle_csp()
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)


    """1.Norweg zamieszkuje pierwszy dom
    2.Anglik mieszka w czerwonym domu.
    3.Zielony dom znajduje się bezpośrednio po lewej stronie domu białego.
    4.Duńczyk pija herbatkę.
    5.Palacz papierosów light mieszka obok hodowcy kotów.
    6.Mieszkaniec żółtego domu pali cygara.
    7.Niemiec pali fajkę.
    8.Mieszkaniec środkowego domu pija mleko.
    9.Palacz papierosów light ma sąsiada, który pija wodę.
    10.Palacz papierosów bez filtra hoduje ptaki.
    11.Szwed hoduje psy.
    12.Norweg mieszka obok niebieskiego domu.
    13.Hodowca koni mieszka obok żółtego domu.
    14.Palacz mentolowych pija piwo.
    15.W zielonym domu pija się kawę."""