using JuMP, GLPK
# prepare a optimized model
m = Model(GLPK.Optimizer)
# declare variables
@variable(m, 0<= x1 <= 10)
@variable(m, x2 >= 0)
@variable(m, x3 >= 0)
# set object
@objective(m, Max, x1  + 2x2 + 5x3)
# add constraints
@constraint(m, constraint1, -x1 + x2  + 3x3 <= -5)
@constraint(m, constraint2, x1 + 3x2 - 7x3 <= 10)
# print prepared optimized model
print(m)
# solve optimization question
JuMP.optimize!(m)
# print the optimal solution
println("Optimal Solution:")
println("x1 = ", JuMP.value(x1))
println("x2 = ", JuMP.value(x2))
println("x3 = ", JuMP.value(x3))
# print the optimal dual variable
println("Dual Variables:")
println("dual1 = ", JuMP.shadow_price(constraint1))
println("dual2 = ", JuMP.shadow_price(constraint2))