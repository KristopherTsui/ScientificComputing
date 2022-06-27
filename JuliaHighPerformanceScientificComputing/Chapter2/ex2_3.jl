using JuMP, GLPK
m = Model(GLPK.Optimizer)
A = [-1 1 3; 1 3 -7]; b = [-5; 10]; c = [1; 2; 5]
# index set
index_x = 1:3; index_constraints = 1:2
# declare variables
@variable(m, x[index_x] >= 0)
# set object
@objective(m, Max, sum(c[i]*x[i] for i in index_x))
# add constraints
@constraint(m, constraint[j in index_constraints], sum(A[j,i]*x[i] for i in index_x) <= b[j])
# add bounded constraint to x[1]
@constraint(m, bound, x[1] <= 10)
# solve optimization problem
JuMP.optimize!(m)
println("Optimal Solution:")
for i in index_x
    println("x[$i] = ", JuMP.value(x[i]))
end
println("Dual Variables:")
for j in index_constraints
    println("dual[$j] = ", JuMP.shadow_price(constraint[j]))
end