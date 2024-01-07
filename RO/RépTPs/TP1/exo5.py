from ortools.linear_solver import pywraplp
def TP1_Exo5():
     # Appel du solver GLOP des problèmes linéaires en nombres réels
     solver = pywraplp.Solver('TP1_Exo5', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
     infinity = solver.infinity()
     # Création des variables réelles
     x = solver.NumVar(0, 4000, 'x')
     y = solver.NumVar(0, 3000, 'y')
     w = solver.NumVar(0, 6000, 'w')
     z = solver.NumVar(0, 5000, 'z')
     a = solver.NumVar(0, 2000, 'a')
     b = solver.NumVar(0, 3000, 'b')
     c = solver.NumVar(0, 2500, 'c')
     print('Nombre des variables =', solver.NumVariables())
     # Minimize z.
     solver.Minimize(1.2*x + 1.5*y + 0.9*w + 1.3*z + 1.45*a +1.2*b + 1*c )
     # Création des contraintes.
     solver.Add( 1*x + 1*y + 1*w + 1*z + 1*a + 1*b + 1*c == 3000)

     solver.Add( 2.5*x + 3*y >= 6000)
     solver.Add( 2.5*x + 3*y <= 9000)

     solver.Add( 0.3*w + 90*z + 96*a + 0.4*b + 0.6*c <= 0.6*3000)
     solver.Add(   0.3*w + 90*z + 96*a + 0.4*b + 0.6*c>=0.4*3000)
     solver.Add(  1.3*x + 0.8*y + 4*a + 1.2*b >= 1.2*3000 )
     solver.Add(  1.3*x + 0.8*y + 4*a + 1.2*b <= 1.65*3000)

     print('Nombre des contraintes =', solver.NumConstraints())
     solver.Solve()
     print('Solution:')
     print('Valeur optimale =', solver.Objective().Value())
     print('x =', x.solution_value())
     print('y =', y.solution_value())
     print('w =', w.solution_value())
     print('z =', z.solution_value())
     print('a =', a.solution_value())
     print('b =', b.solution_value())
     print('c =', c.solution_value())
TP1_Exo5()
