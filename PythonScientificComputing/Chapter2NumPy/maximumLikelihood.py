import numpy as np
import matplotlib.pyplot as plt


def normal_pdf(mean: float, var: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    Calculate the probability density function of a normal distribution.
    """
    return 1 / np.sqrt(2 * np.pi * var) * np.exp(-(x - mean)**2 / (2 * var))


# Generates a random array of normal distributions
# with a standard deviation of 2 and a variance of 4
np.random.seed(20220526)
data = np.random.normal(0, 2.0, size=10)
# calculate the biased sample variance
v1 = np.var(data, ddof=0)  # the default value of ddof is 0
# calculate the unbiased sample variance
v2 = np.var(data, ddof=1)
# calculate the expected value of all these variances
print("The expected value of biased sample variance is ", np.mean(v1))
print("The expected value of unbaised sample variance is ", np.mean(v2))
# produces a set of variance values centered on the variance of the maximum likelihood estimate
var_range = np.linspace(max(v1 - 4, 0.1), v1 + 4, 100)
# calculate the probability density for every sample and every variance
p = normal_pdf(np.mean(data), var_range[:, None], data)
# Find the product of all probability densities along the first axis of p
p = np.product(p, axis=1)

# Plot the likelihood estimates for each variance in var_range
plt.plot(var_range, p)
# unbiased sample variance represented by a vertical line
plt.axvline(v1, 0, 1, c="r")
plt.show()
plt.savefig("maxLikelihood.pdf")