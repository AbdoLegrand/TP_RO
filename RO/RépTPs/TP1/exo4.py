from ortools.linear_solver import pywraplp

def TP1_Exo4():
    # Appel du solver CBC des problèmes linéaires en nombres entiers.
    solver = pywraplp.Solver('TP1_Exo4', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    infinity = solver.infinity()

    # Création des variables entières x et y.
    x = solver.IntVar(0.0, infinity, 'x')
    y = solver.IntVar(0.0, infinity, 'y')
    print('Number of variables =', solver.NumVariables())
    # Création de la fonction objective 50*x + 70*y.
    objective = solver.Objective()
    objective.SetCoefficient(x, 6)
    objective.SetCoefficient(y, 5)
    objective.SetMaximization()
    # Création de la contrainte 20*x + 30*y <= 360.
    ct1 = solver.Constraint(-infinity, 7, 'ct1')
    ct1.SetCoefficient(x, 1)
    ct1.SetCoefficient(y, 3)
    # Création de la contrainte 40*x + 35*y <= 480.
    ct2 = solver.Constraint(-infinity, 9, 'ct2')
    ct2.SetCoefficient(x, 3)
    ct2.SetCoefficient(y, 2)
    print('Number of constraints =', solver.NumConstraints())
    solver.Solve()
    print('Solution:')
    print('Valeur optimale =', solver.Objective().Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())
    print('Advanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())

    
TP1_Exo4()