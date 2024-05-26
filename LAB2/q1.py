import math

def poisson_pmf(x, lmbda):
    return (lmbda**x * math.exp(-lmbda)) / math.factorial(x)

lmbda = 12

for x in range(16):
    probability = poisson_pmf(x, lmbda)
    print(f"P(X = {x}) = {probability:.6f}")