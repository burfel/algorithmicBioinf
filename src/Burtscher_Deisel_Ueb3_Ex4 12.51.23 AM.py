#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# calculate binomial coefficients
def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


# Likelihood function
def LHF(n, k, p):
    probab = choose(n,k) * p**k * (1-p)**(n-k)
    return probab

# try several p-estimators
def searchMax(n, k, p_steps):
    p_vector = [x*(1./p_steps) for x in range(0, p_steps)]
    likelies = []
    for i in range(len(p_vector)):
        likelies.append(LHF(n, k, p_vector[i]))
    to_plot = [p_vector, likelies]
    return to_plot

def plot_graph(to_plot, to_plot2=None):
    plt.close("all")
    plt.figure()
    plt.plot(to_plot[0],to_plot[1],'ko-')
    plt.plot(to_plot2[0],to_plot2[1], 'ro-')
    plt.xlabel('p')
    plt.ylabel('likelihood')
    title = 'Likelihood function for 3 times Zahl and 7 times Kopf (black) \
        \nand for 30 times Zahl and 70 times Kopf (red)'
    plt.title(title)
    plt.savefig('Burtscher_Deisel_Ueb3_Ex4.png')
    plt.show()

if __name__ == '__main__':
    to_plot = searchMax(10, 3, 50)
    to_plot2 = searchMax(100, 30, 50)
    plot_graph(to_plot, to_plot2)

