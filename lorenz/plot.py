"""
This file contains functionalities for plotting

"""
import matplotlib.pyplot as plt


def plot3d(a, b, c, name, s): # make a pdf file for the 3D plot

    # Initialize a figure
    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')
    ax.plot(a, b, c, label='Lorenz attractor')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    if s is True:
        plt.show()

    plt.savefig(name + "/3D.pdf")


def plot2d(a, b, c, name, s): # make a pdf file for three 2D plots
    
    # Initialize a figure
    fig, axs = plt.subplots(3, figsize=(8, 10))
    fig.suptitle('Lorenz Attractor ' + name)

    axs[0].plot(a, b)
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')

    axs[1].plot(a, c)
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Z')

    axs[2].plot(c, b)
    axs[2].set_xlabel('Y')
    axs[2].set_ylabel('Z')

    if s is True:
        plt.show()

    plt.savefig(name + "/2D.pdf")
