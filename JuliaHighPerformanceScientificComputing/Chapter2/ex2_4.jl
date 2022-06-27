"""
Mixed Integer Linear Programming.
"""

using JuMP, GLPK
# prepare a optimized model
m = Model(GLPK.Optimizer)
# declare variables
@variable(m, 0 <= x1 <= 10)
@variable(m, x2 >= 0, Int)
@variable(m, x3, Bin)
# set object
@objective(m, Max, x1 + 2x2 + 5x3)
# add constraints
@constraint(m, constraint1, -x1 + x2 + 3x3 <= -5)
@constraint(m, constraint2, x1 + 3x2 - 7x3 <= 10)
# print prepared optimized model
print(m)
# solve optimization problems
JuMP.optimize!(m)
# print optimal solutions
println("Optimal Solutions:")
println("x1 = ", JuMP.value(x1))
println("x2 = ", JuMP.value(x2))
println("x3 = ", JuMP.value(x3))