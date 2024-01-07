from ortools.linear_solver import pywraplp

def TP1_Exo3():
    # Appel du solver GLOP des problèmes linéaires en nombres réels
    solver = pywraplp.Solver('TP1_Exo3', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    infinity = solver.infinity()
    # Création des variables réelles x et y.
    x = solver.NumVar(0, infinity, 'x')
    y = solver.NumVar(0, infinity, 'y')
    print('Nombre des variables =', solver.NumVariables())
    # Maximize 6*x + 5*y.
    solver.Maximize(6*x + 5*y)
    # Création des contraintes.
    # 1*x + 3*y <= 7.
    solver.Add(1*x + 3*y <= 7)
    # 1*x + 3*y <= 7.
    solver.Add(3*x + 2*y <= 9)
    print('Nombre des contraintes =', solver.NumConstraints())
    solver.Solve()
    print('Solution:')
    print('Valeur optimale =', solver.Objective().Value())
    print('x =', x.solution_value())
    print('y =', y.solution_value())

TP1_Exo3()