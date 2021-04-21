from copy import deepcopy
from typing import Generic, List, Dict, Optional
import random

from constraint import V, D, Constraint


class ConstraintSatisfactionProblem(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]], variable_heuristic="firstUnassigned",
                 domain_heuristic="random"):
        self.variables: List[V] = variables  # variables to be constrained
        self.domains: Dict[V, List[D]] = domains  # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        self.__variable_heuristic = variable_heuristic
        self.__domain_heuristic = domain_heuristic

        self.visited_nodes = 0

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Non existing variable.")
            else:
                self.constraints[variable].append(constraint)

    def check_constraints(self, variable: V, assignment: Dict[V, D]):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned = self.__get_next_unassigned_variable(assignment)

        # get the every possible domain value of the first unassigned variable
        # first: V = unassigned[0]
        for value in self.domains[unassigned]:
            self.visited_nodes += 1
            local_assignment = assignment.copy()
            local_assignment[unassigned] = value
            # if we're still consistent, we recurse (continue)
            if self.check_constraints(unassigned, local_assignment):
                result = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None

    def forward_checking(self, assignment=None):
        result = None
        while result is None:
            result = self.__search_forward_checking(assignment)
        return result

    def __search_forward_checking(self, assignment):
        if assignment is None:
            assignment = {}

        if len(self.variables) == len(assignment):
            return assignment

        self.visited_nodes += 1

        unassigned = self.__get_next_unassigned_variable(assignment)
        values = self.__get_available_domains(assignment, unassigned)

        if len(values) <= 0:
            return None

        assignment[unassigned] = values[0]
        return self.__search_forward_checking(assignment)

    def __get_available_domains(self, assignment, variable):
        results = self.__available_values(self.domains[variable].copy(), assignment)
        if results is None:
            return []

        if len(results) == 0:
            return []

        for val in assignment.values():
            temp_assignment = deepcopy(assignment)
            temp_assignment[variable] = val

            if not self.check_all_constraints_satisfied(variable, temp_assignment):
                if val in results:
                    results.remove(val)

        return results

    def check_all_constraints_satisfied(self, variable: V, assignment: Dict[V, D]):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def __available_values(self, value_domain, assignment):
        if self.__domain_heuristic == "random":
            return self.__random_values(value_domain)
        elif self.__domain_heuristic == "leastUsed":
            return self.__least_used_values(value_domain, assignment, self.__domain_heuristic)
        elif self.__domain_heuristic == "mostUsed":
            return self.__least_used_values(value_domain, assignment, self.__domain_heuristic)

    def __get_next_unassigned_variable(self, assignment):
        if self.__variable_heuristic == "firstUnassigned":
            return self.__first_unassigned_variable(assignment)
        elif self.__variable_heuristic == "mostConstraints":
            return self.__get_constraint_variable(assignment, self.__variable_heuristic)
        elif self.__variable_heuristic == "leastConstraints":
            return self.__get_constraint_variable(assignment, self.__variable_heuristic)

    def __first_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable
        return None

    def __get_constraint_variable(self, assignment, heuristic):
        unassigned = [variable for variable in self.variables if variable not in assignment]
        variable_constraints = 0
        variable_with_most_constraints = None

        for variable in unassigned:
            amount = len(self.constraints[variable])
            if heuristic == "mostConstraints":
                if amount > variable_constraints:
                    variable_constraints = amount
                    variable_with_most_constraints = variable
            else:
                if amount < variable_constraints:
                    variable_constraints = amount
                    variable_with_most_constraints = variable

        if variable_with_most_constraints == None:
            variable_with_most_constraints = unassigned[0]

        return variable_with_most_constraints

    @staticmethod
    def __random_values(domain):
        random.shuffle(domain)
        return domain

    @staticmethod
    def __least_used_values(domain, assignment, heuristic):
        values_with_amount = {}
        for d in domain:
            values_with_amount[d] = 0

        for d in assignment.values():
            values_with_amount[d] += 1

        values = []
        l = list(values_with_amount.items())
        random.shuffle(l)
        values_with_amount = dict(l)
        while len(values_with_amount) > 0:
            if heuristic == "leastUsed":
                value = min(values_with_amount, key=values_with_amount.get)
            else:
                value = max(values_with_amount, key=values_with_amount.get)
            values.append(value)
            values_with_amount.pop(value)
        return values
