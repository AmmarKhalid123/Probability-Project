import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sympy import Point, Line, Eq

def task_eight():
    theta = np.linspace(0, 2*np.pi, 100)
    r = np.sqrt(10000)

    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)

    fig, ax = plt.subplots(1)

    ax.plot(x1, x2)

    # For start postion of two points

    # for point_one
    point_one_x = list(np.random.uniform(0, 100, size = 1))
    point_one_y = list(np.random.uniform(0, 100, size = 1))
    while ( ((point_one_y[0])**2) + ((point_one_x[0])**2) >= 10000):
        point_one_y = list(np.random.uniform(0, 100, size = 1))
        point_one_x = list(np.random.uniform(0, 100, size = 1))    

    # for point_two
    point_two_x = list(np.random.uniform(0, 100, size = 1))
    point_two_y = list(np.random.uniform(0, 100, size = 1))
    while ( ((point_two_y[0])**2) + ((point_two_x[0])**2) >= 10000):
        point_two_y = list(np.random.uniform(0, 100, size = 1))
        point_two_x = list(np.random.uniform(0, 100, size = 1))

    new_theta_one = list(np.random.uniform(0, 2*np.pi, size=1))
    r_one = np.random.uniform(0, 1, size=1)[0]

    new_theta_two = list(np.random.uniform(0, 2*np.pi, size=1))
    r_two = np.random.uniform(0, 1, size=1)[0]

    def end_case(x_one, y_one, x_two, y_two):        
        if np.sqrt((x_one - x_two)**2 + (y_one - y_two)**2) <= 1:
            return True
        return False

    steps = 0

    while True:
        steps += 1

        if steps > 20000:
            break

        x_one_pos = r_one * np.cos( np.cumsum(new_theta_one)[-1])
        y_one_pos = r_one * np.sin( np.cumsum(new_theta_one)[-1])        

        x_two_pos = r_two * np.cos( np.cumsum(new_theta_two)[-1])
        y_two_pos = r_two * np.sin( np.cumsum(new_theta_two)[-1])

        main_x_one = x_one_pos + point_one_x[-1]
        main_y_one = y_one_pos + point_one_y[-1]
        main_x_two = x_two_pos + point_two_x[-1]
        main_y_two = y_two_pos + point_two_y[-1]

        if (main_x_one)**2 + (main_y_one)**2 <= 10000:
            point_one_x.append(main_x_one)
            point_one_y.append(main_y_one)

        if (main_x_two)**2 + (main_y_two)**2 <= 10000:
            point_two_x.append(main_x_two)
            point_two_y.append(main_y_two)

        if end_case(point_one_x[-1], point_one_y[-1], point_two_x[-1], point_two_y[-1]):
            break

        new_theta_one.append(np.random.uniform(0, 2*np.pi, size=1)[0])
        new_theta_two.append(np.random.uniform(0, 2*np.pi, size=1)[0])

        r_one = np.random.uniform(0, 1, size=1)[0]
        r_two = np.random.uniform(0, 1, size=1)[0]
    print('Both point started at ( {}, {}) and ( {}, {})'.format(round(point_one_x[0], 2), round(point_one_y[0], 2) , round(point_two_x[0], 2), round(point_two_y[0], 2)))
    if steps <= 20000:
        print('Coincide after', steps,'steps')
    else:
        print('Points did not coincide')
    print('Both point ended at ( {}, {}) and ( {}, {})'.format(round(point_one_x[-1], 2), round(point_one_y[-1], 2), round(point_two_x[-1], 2), round(point_two_y[-1]), 2))
    

    ## comment these two lines for animation 1/2
    ax.plot(point_one_x, point_one_y)
    ax.plot(point_two_x, point_two_y)

    ax.set_aspect(1)

    plt.grid(linestyle='--')

    plt.title('Task Eight', fontsize=8)

    ## uncomment below lines for animation 2/2
    # x_Adata, y_Adata, x_Bdata, y_Bdata = [], [], [], []
    # ln, = plt.plot(x_Adata, y_Adata, 'b-')
    # ln2, = plt.plot(x_Bdata, y_Bdata, 'r-')

    # def init():
    #     ax.set_xlim(-110, 110)

    #     ax.set_ylim(-110, 110)
    #     ln.set_data([], [])
    #     ln2.set_data([], [])
    #     return ln, ln2,

    # def update(frame):
    #     x_Adata.append(point_one_x[int(frame)])
    #     y_Adata.append(point_one_y[int(frame)])
    #     x_Bdata.append(point_two_x[int(frame)])
    #     y_Bdata.append(point_two_y[int(frame)])
    #     ln.set_data(x_Adata, y_Adata)
    #     ln2.set_data(x_Bdata, y_Bdata)
    #     return ln, ln2,
    # if len(point_one_x) > len(point_two_x):
    #     ani = FuncAnimation(fig, update, frames=np.linspace(0, len(point_two_x)-1, num=len(point_two_x)), interval=10,
    #                         init_func=init, blit=False, repeat=False)
    # else:
    #     ani = FuncAnimation(fig, update, frames=np.linspace(0, len(point_one_x)-1, num=len(point_one_x)), interval=10,
    #                         init_func=init, blit=False, repeat=False)

    plt.show()

task_eight()
