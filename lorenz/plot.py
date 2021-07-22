"""
This file contains functionalities for plotting

"""
import matplotlib.pyplot as plt


def plot3d(a, b, c, name, s):
    """
    This function creates a 3D plot (x-y-z) and stores the figure as PDF

    INPUT::

     a: first variable as array
     b: second variable as array
     c: third variable as array
     name: name for making the title etc.
     s: if True then the plot will be shown (to continue execution close the plot window)

    OUPUT::

     stores a figure in /name/3dplot.pdf

    """

    # Initialize a figure
    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')
    ax.plot(a, b, c, label='Lorenz attractor')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    if s is True:
        plt.show()

    plt.savefig(name + "/3dplot.pdf")


def plot2d(a, b, c, name, s):
    """
    This function creates three subplots (x-y, x-z, y-z) and stores the figure as PDF

    INPUT::

     a: first variable as array
     b: second variable as array
     c: third variable as array
     name: name for making the title etc.
     s: if True then the plot will be shown (to continue execution close the plot window)

    OUPUT::

     stores a figure in /name/2dplot.pdf

    """

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

    plt.savefig(name + "/2dplot.pdf")
