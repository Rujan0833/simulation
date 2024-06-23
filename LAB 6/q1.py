#WAP to generate 50 random numbers using Mixed Congruential Method  where X0=11, m=100, a = 5 and c = 13.  

def mixed_congruential_generator(seed, m, a, c, num_samples):
    """
    Generate random numbers using the Mixed Congruential Method.
    
    Args:
    seed (int): The initial seed value (X0)
    m (int): The modulus
    a (int): The multiplier
    c (int): The increment
    num_samples (int): The number of random numbers to generate
    
    Returns:
    list: A list of generated random numbers
    """
    random_numbers = []
    x = seed
    
    for _ in range(num_samples):
        x = (a * x + c) % m
        random_numbers.append(x)
    
    return random_numbers

# Parameters
X0 = 11  # Initial seed
m = 100  # Modulus
a = 5    # Multiplier
c = 13   # Increment
num_samples = 50  # Number of random numbers to generate

# Generate random numbers
random_numbers = mixed_congruential_generator(X0, m, a, c, num_samples)

# Print the generated random numbers
print("Generated random numbers:")
for i, num in enumerate(random_numbers, 1):
    print(f"{i}: {num}")