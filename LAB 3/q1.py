import random
import math

def estimate_pi(num_points):
    inside_count = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            inside_count += 1

    pi_estimate = 4 * inside_count / num_points
    return pi_estimate

num_points = 1000000
estimated_pi = estimate_pi(num_points)
print(f"Estimated value of π using {num_points} points: {estimated_pi}")