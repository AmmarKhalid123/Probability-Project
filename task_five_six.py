import numpy as np
import matplotlib.pyplot as plt

def task_five_six(steps=100):
    theta = np.linspace(0, 2*np.pi, 100)
    r = np.sqrt(25.0)

    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)

    fig, ax = plt.subplots(1)

    ax.plot(x1, x2)

    xx = [0]
    yy = [0]

    new_theta = np.cumsum(np.random.uniform(0, 2*np.pi, size=steps))
    new_r = np.random.uniform(0, 1, size=steps)

    def in_range(x, y):
        if (x*x) + (y*y) <= 25:
            return x, y
        return False, False

    for a, b in zip(new_theta, new_r):
        x_pos = b*np.cos(a)
        y_pos = b*np.sin(a)
        main_x, main_y = in_range(xx[-1] + x_pos, yy[-1] + y_pos)
        if main_x != False:
            xx.append(main_x)
            yy.append(main_y)

    ax.plot(xx, yy)

    ax.set_aspect(1)

    plt.xlim(-7,7)
    plt.ylim(-7,7)

    plt.grid(linestyle='--')

    plt.title('Task Five/Six', fontsize=8)

    plt.show()
task_five_six(200)