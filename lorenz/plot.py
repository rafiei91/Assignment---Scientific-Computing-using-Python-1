"""
This file contains functionalities for plotting
"""

import matplotlib.pyplot as plt

def plot_3D(a, b, c, case, s): # make a pdf file for the 3D plot

    fig = plt.figure()
    
    ax = fig.add_subplot(projection='3d')
    ax.plot(a, b, c, color='r', linewidth=0.05)
    fig.suptitle('3D Lorenz Attractor plot for ' + case)

    ax.set(xlabel='x', ylabel='y', zlabel='z')

    plt.savefig(case + "/" + case + " - 3D.pdf")

def plot_2D(a, b, c, case, s): # make a pdf file for three 2D plots
    
    fig, axs = plt.subplots(3, figsize=(8, 10))
    fig.suptitle('2D Lorenz Attractor plot for ' + case)

    axs[0].plot(a, b, color='r', linewidth=0.05)
    axs[0].set(xlabel='x', ylabel='y', title='(x-y) plot')

    axs[1].plot(a, c, color='r', linewidth=0.05)
    axs[1].set(xlabel='x', ylabel='z', title='(x-z) plot')

    axs[2].plot(b, c, color='r', linewidth=0.05)
    axs[2].set(xlabel='y', ylabel='z', title='(y-z) plot')

    fig.subplots_adjust(hspace=0.5)

    plt.savefig(case + "/" + case + " - 2D.pdf")
