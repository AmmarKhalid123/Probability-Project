# Python code for 1-D random walk. 
import random 
import numpy as np 
import matplotlib.pyplot as plt 

'''
args -  1) p (probability of going left)
        2) start (starting point) 
        3) steps (total steps to be taken)  
'''
def task_one(p, start, steps):
    probability = [p, 1 - p]
    x_axis = [start]
    y_axis = list(range(steps+1))
    for random_p in np.random.random(steps):
        if random_p < p:
            x_axis.append(x_axis[-1]-1)    
        if random_p > p:
            x_axis.append(x_axis[-1]+1)
    plt.plot(x_axis, y_axis)
    plt.show()

## SCENARIO-1: HIGH PROBABILITY OF GOING LEFT
# task_one(0.8, 0, 100)
## SCENARIO-2: HIGH PROBABILITY OF GOING RIGHT
# task_one(0.2, 0, 100)

## SCENARIO-3: EQUAL PROBABILITY OF GOING LEFT AND RIGHT
# task_one(0.5, 0, 100)

## SCENARIO-4: ZERO PROBABILITY OF GOING RIGHT
# task_one(1.0, 0, 100)
## SCENARIO-5: ZERO PROBABILITY OF GOING LEFT
# task_one(0.0, 0, 100)
