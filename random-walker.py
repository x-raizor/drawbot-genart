# Random Walker
# version 3

from random import seed, randrange
from numpy.random import choice
from numpy.random import seed as seed_np

seed_value = 3
line_color = (1.00, 0.95, 0.36)
step_length_max = 5
step_length_min = 1
step_length_step = 1
step_amount = 15450
current_position = (0, 0)
directions = ['north', 'west', 'east',  'south','ne', 'sw', 'nw', 'se']
probability_gap = 0.125 
prev_direction = directions[0]

seed(seed_value)
seed_np(seed_value)
size(800, 800)

def fill_probes(prev_direction, directions = directions, prob_gap = probability_gap):
    idx = directions.index(prev_direction)
    probs = [1 / len(directions) + prob_gap / (len(directions) - 1)] * (len(directions)) 
    probs[idx] = 1 / len(directions) - prob_gap
    return probs
    
# ...
# background
fill(0.14, 0.15, 0.16)
rect(0, 0, width(), height())

translate(width()/2, height()/2)

newPath()
moveTo(current_position)

fill(None)
stroke(line_color[0], line_color[1], line_color[2])
strokeWidth(0.1)

for step in range(step_amount):
    direction = choice(directions, p = fill_probes(prev_direction))
    step = randrange(step_length_min, step_length_max, step_length_step)
    if direction == 'north':
        current_position = (
            current_position[0], 
            current_position[1] + step)
    elif direction == 'east':
        current_position = (
            current_position[0] + step, 
            current_position[1])
    elif direction == 'south':
        current_position = (
            current_position[0], 
            current_position[1] - step)
    elif direction == 'ne':
        current_position = (
            current_position[0] + 0.71*step, 
            current_position[1] + 0.71*step)
    elif direction == 'sw':
        current_position = (
            current_position[0] - 0.71*step, 
            current_position[1] - 0.71*step)

    elif direction == 'nw':
        current_position = (
            current_position[0] - 0.71*step, 
            current_position[1] + 0.71*step)
    elif direction == 'se':
        current_position = (
            current_position[0] + 0.71*step, 
            current_position[1] - 0.71*step)
    else: # west
        current_position = (
            current_position[0] - step, 
            current_position[1])
            
    prev_direction = direction
    lineTo(current_position) 
    
drawPath()