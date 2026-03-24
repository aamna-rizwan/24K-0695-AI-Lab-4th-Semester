#task 6
from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = model.new_int_var(0, 20, "x")
y = model.new_int_var(0, 20, "y")
z = model.new_int_var(0, 20, "z")

# Constraints
model.add(x + 2*y + z <= 20)
model.add(3*x + y <= 18)

# Objective
model.maximize(4*x + 2*y + z)

solver = cp_model.CpSolver()
status = solver.solve(model)

if status == cp_model.OPTIMAL:
    print("Optimal Value =", solver.objective_value)
    print("x =", solver.value(x))
    print("y =", solver.value(y))
    print("z =", solver.value(z))
