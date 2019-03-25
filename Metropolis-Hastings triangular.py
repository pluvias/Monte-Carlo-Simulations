# Simulating the triangular distribution with Metropolis-Hastings algorithm.
# Compared with the simple simulation using formula for generating random variables.

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# The probability density function (PDF):
def triangular(q, alpha, beta): return (2*(1-np.abs(alpha+beta-2*q)/(beta-alpha)))/(beta-alpha)


N = 1000  # Sample length
alpha, beta = 16, 36  # Parameters. Given: (betta-alpha) > 0.
X = []
x = np.linspace(alpha, beta, 1000)


for i in range(N):
    X.append(alpha + 0.5*(beta-alpha)*(np.random.rand()+np.random.rand()))  # generate random variables


def metropolis_hastings(samples, p, a, b, sigma=1):
    '''

    The Metropolis–Hastings algorithm samples from p using normal distribution
    At each iteration, the algorithm picks a candidate for the next sample value based on the current sample value.
    Then, with some probability, the candidate is either accepted
    (in which case the candidate value is used in the next iteration) or rejected
    (in which case the candidate value is discarded, and current value is reused in the next iteration)
    https://en.wikipedia.org/wiki/Metropolis-Hastings_algorithm

    :param samples: number of samples
    :param p: a target distribution with parameters a, b to sample from
    :param sigma: standard deviation of a normal distribution
    '''

    posterior = np.zeros(samples)
    u = np.random.uniform(size=samples)  # uniform samples
    current = np.random.uniform()  # arbitrary point, the 1st sample
    rv = norm.rvs(size=samples, scale=sigma)  # random variates of given type for tuning the random walk

    curr_poster = p(current, a, b) * norm.pdf(current, loc=0, scale=2)  # current posterior

    for i in range(samples):
        x_prop = current + rv[i]

        prop_poster = p(x_prop, a, b) * norm.pdf(x_prop, loc=0, scale=2)  # proposed posterior

        # calculate the acceptance ratio,
        # which will be used to decide whether to accept or reject the candidate:
        alpha = prop_poster / curr_poster

        if u[i] <= alpha:  # accept the candidate
            current = x_prop
            curr_poster = prop_poster

        posterior[i] = current

    return posterior

Y = metropolis_hastings(N, triangular, alpha, beta)

fig, ax = plt.subplots(1, 2)
ax[0].hist(X, density=True, bins=25, color='C0')
ax[1].hist(Y, density=True, bins=25, color='C1')
plt.show()
