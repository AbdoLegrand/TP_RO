from ortools.linear_solver import pywraplp
def EX01():
    # Appel du solver CBC des problèmes linéaires en nombres entiers.
    solver = pywraplp.Solver('EXO1', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    infinity = solver.infinity()

    max_mang = 1.65
    n=7
    Stocke = [4000, 3000, 6000, 5000, 2000, 3000, 2500]
    cout = [1.2, 1.5, 0.9, 1.3, 1.45, 1.2, 1]
    Manganese = [1.3, 0.8,0, 0, 4, 1.2, 0]
    cuivre = [0, 0,0.3, 90, 96, 0.4, 0.6]
    Carb = [2.5, 3, 0, 0, 0, 0, 0]
    X = []

    objective = solver.Objective()
    ct_1 = solver.Constraint(3000, 3000, 'ct_1')
    ct_2 = solver.Constraint(6000, 9000, 'ct_2')
    ct_3 = solver.Constraint(0.4*3000, 0.6*3000, 'ct_3')
    ct_4 = solver.Constraint(1.2*3000, 1.65*3000, 'ct4')

    for i in range(n):
        x = solver.NumVar(0, Stocke[i], 'x_'+str(i))
        X.append(x)
    print('Number of variables =', solver.NumVariables())

    objective = solver.Objective()
    
    for i in range(n):
        objective.SetCoefficient(X[i], cout[i])
    objective.SetMinimization()

    for i in range(n):
        objective.SetCoefficient(X[i], cout[i])
        ct_1.SetCoefficient(X[i], 1)
        ct_2.SetCoefficient(X[i], Carb[i])
        ct_3.SetCoefficient(X[i], cuivre[i])
        ct_4.SetCoefficient(X[i], Manganese[i])

    objective.SetMinimization()

    print('Number of constraints =', solver.NumConstraints())
    solver.Solve()
    print('Solution:')
    print('Valeur optimale =', solver.Objective().Value())
    
    for i in range(n):
        print('x',i,' =', X[i].solution_value())
       


   
    print('Advanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())

EX01()