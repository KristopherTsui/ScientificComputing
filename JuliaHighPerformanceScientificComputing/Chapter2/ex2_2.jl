using JuMP, GLPK
m = Model(GLPK.Optimizer)
# 上述线性规划问题的另一种表达方式
@variable(m, x[1:3] >= 0)
A = [-1 1 3; 1 3 -7]; b = [-5; 10]; c = [1; 2; 5]
# set object
@objective(m, Max, sum(c[i]*x[i] for i = 1:3))
# add constraints
# @constraint(m, constraint1, sum(A[1,i]*x[i] for i = 1:3) <= b[1])
# @constraint(m, constraint2, sum(A[2,i]*x[i] for i = 1:3) <= b[2])
# 上述限定条件的方式只适合少量的情况，对于大量的限定条件，应该使用如下方式
# constraint = Dict()
# for j = 1:2
    # constraint[j] = @constraint(m, sum(A[j,i]*x[i] for i = 1:3) <= b[j]);
# end
# 或者还有一种更好的方式
@constraint(m, constraint[j = 1:2], sum(A[j,i]*x[i] for i = 1:3) <= b[j])
# add bounded constraint to x1
@constraint(m, bound, x[1] <= 10)
# solve optimization problems
JuMP.optimize!(m)
println("Optimal Solutions:")
for i = 1:3
    println("x[$i] = ", JuMP.value(x[i]))
end
println("Dual Variables:")
for j = 1:2
    println("dual[$j] = ", JuMP.shadow_price(constraint[j]))
end