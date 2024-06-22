import math

lambda_val = 12
poisson_probabilities = []

for x in range(16):
    probability = (math.exp(-lambda_val) * (lambda_val ** x)) / math.factorial(x)
    poisson_probabilities.append(probability)

header = f"{'x':<5} {'f(x)':<15}"
print(header)
print("=" * len(header))
for x, prob in enumerate(poisson_probabilities):
    print(f"{x:<5} {prob:<15.10f}")
