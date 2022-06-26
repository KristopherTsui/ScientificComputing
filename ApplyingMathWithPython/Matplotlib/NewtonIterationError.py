from matplotlib import pyplot as plt


def generate_newton_iters(x0, number):
    iterates = [x0]
    errors = [abs(x0 - 1.)]
    for _ in range(number):
        x0 = x0 - (x0 * x0 - 1.) / (2 * x0)
        iterates.append(x0)
        errors.append(abs(x0 - 1.))
    return iterates, errors


iterates, errors = generate_newton_iters(2.0, 5)

# parameter tigiht_layout=True:
# ignore left and right and adjust subplot sizes to fill the figure
fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)

ax1.plot(iterates, marker="x", linestyle="none")
ax1.set_title("Iterates")
ax1.set_xlabel("$i$", usetex=True)
ax1.set_ylabel("$x_i$", usetex=True)

ax2.semilogy(errors, marker="x", linestyle="none")
ax2.set_title("Error")
ax2.set_xlabel("$i$", usetex=True)
ax2.set_ylabel("Error")

plt.show()