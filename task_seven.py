import numpy as np
import matplotlib.pyplot as plt


def task_seven():
    theta = np.linspace(0, 2*np.pi, 100)
    r = np.sqrt(25.0)

    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)

    fig, ax = plt.subplots()

    ax.plot(x1, x2)

    xx = [0]
    yy = [0]

    new_theta = np.cumsum(np.random.uniform(0, 2*np.pi, size=100))
    new_r = np.random.choice([0, 0.5, 1, ], 100)


    for a, b in zip(new_theta, new_r):
        x_pos = b*np.cos(a)
        y_pos = b*np.sin(a)
        xx.append(xx[-1] + x_pos)
        yy.append(yy[-1] + y_pos)


    # xx = np.cumsum(xx)
    # yy = np.cumsum(yy)

    # def in_range(x, y, a, b):
    #     if (x*x) + (y*y) <= 25:
    #         return True
    #     return False

        
    ax.plot(xx, yy)

    ax.set_aspect(1)

    plt.xlim(-7,7)
    plt.ylim(-7,7)

    plt.grid(linestyle='--')

    plt.title('How to plot a circle with matplotlib ?', fontsize=8)

    plt.show()