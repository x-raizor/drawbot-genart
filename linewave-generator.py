# Waving Lines Generator
# version 1.1

from random import random, randrange, seed

w = 1600
h = 720

seed_value = 4
lines_amount = 2
duplicate_amount = 10
segment_number_max = 3
segment_number_min = 1
stroke_width_min = 2
stroke_width_max = 6
stroke_alpha_min = 0.95
stroke_alpha_max = 1
line_color = (1.00, 0.85, 0.36)  # 1.00, 0.95, 0.36
red_var = 0.8
green_var = 0.85
blue_var = 0.80
x_jitter = 90
y_jitter = 63
bubble_jitter_scale = 5
h_amp = 90
h_var = 480
h_padding = 570
freeze_randomness = True
randomize_height = False
with_bubbles = False


def segment(p1, h1, h2, p2): 
    # point 1, handle1, handle2, point2

    newPath()
    moveTo(p1)
    curveTo(h1, h2, p2)
    drawPath()

    if with_bubbles:
        
        if (random() > 0.62):
 #           fill(line_color[0], line_color[1], line_color[2]); stroke(None)
            oval(
    h1[0] - (0.5-random()) * x_jitter * bubble_jitter_scale, 
    h1[1] - (0.5-random()) * y_jitter * bubble_jitter_scale, 2, 2)
            oval(
    h2[0] - (0.5-random()) * x_jitter * bubble_jitter_scale, 
    h2[1] - (0.5-random()) * y_jitter * bubble_jitter_scale, 2, 2)
#            fill(None)

def ecurve(
        height = 100, 
        h_amp = 90, 
        h_var = 120, 
        segment_number = 5):

    segment_step = width() / (0.0 + segment_number)
    handle_step = segment_step / 3
    
    p1_ = []; p2_ = []; h1_ = []; h2_ = []
    for i in range(segment_number):
        x_base = i * segment_step
        h_diff = h_amp - h_var
        p1 = (x_base, height)
        if i == 0:
            h1 = (x_base + handle_step, 
                  height + h_diff + h_var * random())
        else:
            h1 = (2*p1[0] - prev_handle[0], 
                 (2*p1[1] - prev_handle[1]))
            
        h2 = prev_handle = (x_base + 2 * handle_step, 
              height - h_diff - h_var * random())
        p2 = (x_base + segment_step, height)
        p1_.append(p1)
        p2_.append(p2)
        h1_.append(h1)
        h2_.append(h2)
        
    # cycle for line duplicates
    for j in range(duplicate_amount):
        x_shift = x_jitter / 2 - random() * x_jitter
        y_shift = y_jitter / 2 - random() * y_jitter
        translate(x_shift, y_shift)
        
        # line properties
        # precalc
        alpha = stroke_alpha_min + \
            (stroke_alpha_max - stroke_alpha_min) * random()
        (red, green, blue) = (
            line_color[0] - red_var *(0.5 - random()),
            line_color[1] - green_var *(0.5 - random()),
            line_color[2] - blue_var *(0.5 - random()))
        
        # fulfil
        fill(None)
        stroke(red, green, blue, alpha)
        strokeWidth(randrange(stroke_width_min, stroke_width_max))
        
        # print line by segments
        for i in range(segment_number):
            segment(p1_[i], h1_[i], h2_[i], p2_[i])

        translate(-x_shift, -y_shift)
            
# ...
# Start 

size(w, h)

if freeze_randomness:
    seed(seed_value)
    
# background
fill(0.14, 0.15, 0.16)
rect(0, 0, w, h)

for x in range(lines_amount):
    if randomize_height:
        h = h_padding / 2 + (height() - h_padding) * random()
    else:
        h = height() / 2
    ecurve(
        height = h, 
        h_amp = h_amp,
        h_var = h_var,
        segment_number = \
            randrange(segment_number_min, segment_number_max))
        
# Debug
#text(str(round(h_amp)) + ', ' + str(round(h_var)), (10, 10))
