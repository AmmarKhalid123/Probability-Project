import numpy as np
import matplotlib.pyplot as plt

def task_three():
    theta = np.linspace(0, 2*np.pi, 100)
    radius = np.sqrt(25.0)

    x1 = radius*np.cos(theta)
    x2 = radius*np.sin(theta)

    fig, ax = plt.subplots(1)

    ax.plot(x1, x2)

    def in_range(new_x, new_y):
        if (new_x*new_x) + (new_y*new_y) <= 25:
            return new_x, new_y
        else:            
            return False, False

    xx = [0]
    yy = [0]

    discrete_angles = [0, (np.pi / 4), (np.pi / 2), ((3*np.pi) / 4), (np.pi), ((5*np.pi) / 4), ((3*np.pi) / 2), ((7*np.pi) / 4), (2 * np.pi), ]

    new_theta = np.cumsum(np.random.choice(discrete_angles, 200))
    new_r = np.random.choice([0.0, 1.0, 0.5, ], 200)


    for a, b in zip(new_theta, new_r):
        x_pos = b*np.cos(a)
        y_pos = b*np.sin(a)
        main_x, main_y = in_range(xx[-1] + x_pos, yy[-1] + y_pos)
        if main_x != False:
            xx.append(xx[-1] + x_pos)
            yy.append(yy[-1] + y_pos)

    ax.plot(xx, yy)

    ax.set_aspect(1)

    plt.xlim(-7,7)
    plt.ylim(-7,7)

    plt.grid(linestyle='--')

    plt.title('Task Three', fontsize=8)

    plt.show()

task_three()
