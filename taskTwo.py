import random 
import numpy as np 
import matplotlib.pyplot as plt


'''
args -  1) p_one (probability of pt. one of going left)
        2) p_two (probability of pt. two of going left)
        3) start_one (starting pt. of pt. one)
        4) start_two (starting pt. of pt. two)
'''
def task_two(p_one, p_two, start_one, start_two):
    x_axis_one = [start_one]
    x_axis_two = [start_two]
    
    steps = 0
    while True:

        if x_axis_one[-1] == x_axis_two[-1]:
            print("Both point meets at " + str(steps) + " seconds.")
            break
        steps += 1

        random_p = np.random.random(1)[0]
        if random_p < p_one:
            x_axis_one.append(x_axis_one[-1] - 1)
        if random_p > p_one:
            x_axis_one.append(x_axis_one[-1] + 1)
        
        random_p = np.random.random(1)[0]
        if random_p < p_two:
            x_axis_two.append(x_axis_two[-1] - 1)
        if random_p > p_two:
            x_axis_two.append(x_axis_two[-1] + 1)
    y_axis = list(range(steps+1))        
    plt.plot(x_axis_one, y_axis, 'b-', label='First Point')
    plt.plot(x_axis_two, y_axis, 'r-', label='Second Point')
    plt.legend()
    plt.show()



task_two(0.7, 0.3, 0, 0)