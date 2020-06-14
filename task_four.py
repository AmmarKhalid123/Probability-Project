import random 
import numpy as np 
import matplotlib.pyplot as plt 

'''
args -  1) p (probability of going left)
        2) start (starting point) 
        3) steps (total steps to be taken)  
# '''
def task_four(p, start, steps):
    probability = [p, 1 - p]
    x_axis = [start]
    y_axis = list(range(steps+1))
    for random_p in np.random.random(steps):
        if random_p < p:
            x_axis.append(x_axis[-1] - np.random.random(1)[0])    
        if random_p > p:
            x_axis.append(x_axis[-1] + np.random.random(1)[0])
    plt.plot(x_axis, y_axis)
    plt.show()

task_four(0.5, 0, 100)