import random
import math

def function(x):
    return x**2  

def estimate_area(num_points, a, b):
    area = 0
    for _ in range(num_points):
        x = random.uniform(a, b)
        y = random.uniform(0, function(b))
        if y <= function(x):
            area += 1

    area = (b - a) * function(b) * (area / num_points)
    return area


a = 0  
b = 2  
num_points = 100
estimated_area = estimate_area(num_points, a, b)
print(f"Estimated area under the curve using {num_points} points: {estimated_area}")