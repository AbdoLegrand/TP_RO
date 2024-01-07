from ortools.linear_solver import pywraplp
from ortools.linear_solver.pywraplp import Objective


def exo1():
    solver = pywraplp.Solver('exo1', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    D = 3000
    obj = [1.2, 1.5, 0.9, 1.3, 1.45, 1.2, 1]

    max_mang = 1.65
    min_mang = 1.2
    mang = [1.3, 0.8, 0, 0, 4, 1.2, 0]

    max_cu = 0.6
    min_cu = 0.4
    cu = [0, 0, 0.3, 90, 96, 0.4, 0.6]

    max_cr = 3
    min_cr = 2
    cr = [2.5, 3, 0, 0, 0, 0, 0]

    # Contrainte de disponibilité des stockes
    X = []
    max_x = [4000, 3000, 6000, 5000, 2000, 3000, 2500]

    # Creation des variables de décision x1, x2 ....
    for i in range(7):
        x = solver.NumVar(0, max_x[i], 'x'+str(i+1))
        X.append(x)
    objective = solver.Objective()

    for i in range(7):
        objective.SetCoefficient(X[i], obj[i])
    objective.SetMinimization()

    # Création des contraintes.

    # Contrainte de satisfaction de la demande
    ct_D = solver.Constraint(D, D, 'ct_D')

    # Contrainte de respect du pourcentage de Manganèse
    ct_mang = solver.Constraint(min_mang * D, max_mang * D, 'ct_mang')

    # Contrainte de respect du pourcentage de cuivre
    ct_cu = solver.Constraint(min_cu * D, max_cu * D, 'ct_cu')

    # Contrainte de respect du pourcentage de carbone
    ct_cr = solver.Constraint(min_cr * D, max_cr * D, 'ct_cr')

    for i in range(7):
        ct_D.SetCoefficient(X[i], 1)
        ct_mang.SetCoefficient(X[i], mang[i])
        ct_cu.SetCoefficient(X[i], cu[i])
        ct_cr.SetCoefficient(X[i], cr[i])

    solver.Solve()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    print('Solution:')
    print('Valeur optimale =', solver.Objective().Value())

    for i in range(7):
        print('x', i, ' = ', X[i].solution_value())

    print('Advanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())

exo1()
