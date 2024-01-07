from ortools.linear_solver import pywraplp

def TP1_Exo5():
    # Appel du solver GLOP des problèmes linéaires en nombres réels
    solver = pywraplp.Solver('TP1_Exo5', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    infinity = solver.infinity()
    # Création des variables réelles x1 ... x7 .
    x1 = solver.NumVar(0, infinity, 'x')
    x2 = solver.NumVar(0, infinity, 'x2')
    x3 = solver.NumVar(0, infinity, 'x3')
    x4 = solver.NumVar(0, infinity, 'x4')
    x5 = solver.NumVar(0, infinity, 'x5')
    x6 = solver.NumVar(0, infinity, 'x6')
    x7 = solver.NumVar(0, infinity, 'x7')
    print('Nombre des variables =', solver.NumVariables())
    # Minimize 1.2*x1 + 1.5*x2 + 0.9*x3 + 1.3*x4 + 1.45*x5 + 1.2*x6 + x7.
    solver.Minimize(1.2*x1 + 1.5*x2 + 0.9*x3 + 1.3*x4 + 1.45*x5 + 1.2*x6 + x7)
    # Création des contraintes.
    # x1 <= 4000.
    solver.Add(x1 <= 4000)
    # x2 <= 3000.
    solver.Add(x2 <= 3000)
    # x3 <= 6000.
    solver.Add(x3 <= 6000)
    # x4 <= 5000.
    solver.Add(x4 <= 5000)
    # x5 <= 2000.
    solver.Add(x5 <= 2000)
    # x6 <= 3000.
    solver.Add(x6 <= 3000)
    # x7 <= 2500.
    solver.Add(x7 <= 2500)

    print('Nombre des contraintes =', solver.NumConstraints())
    solver.Solve()
    print('Solution :')
    print('Valeur optimale =', solver.Objective().Value())
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())
    print('x3 =', x3.solution_value())
    print('x4 =', x4.solution_value())
    print('x5 =', x5.solution_value())
    print('x6 =', x6.solution_value())
    print('x7 =', x7.solution_value())


TP1_Exo5()