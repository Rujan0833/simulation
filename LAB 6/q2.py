#WAP to generate 50 random numbers using Multiplicative Congruential  Method where X0=13, m =1000, a = 15 and c = 7.

def multiplicative_congruential_generator(seed, m, a, num_samples):
    """
    Generate random numbers using the Multiplicative Congruential Method.
    
    Args:
    seed (int): The initial seed value (X0)
    m (int): The modulus
    a (int): The multiplier
    num_samples (int): The number of random numbers to generate
    
    Returns:
    list: A list of generated random numbers
    """
    random_numbers = []
    x = seed
    
    for _ in range(num_samples):
        x = (a * x) % m
        random_numbers.append(x)
    
    return random_numbers

# Parameters
X0 = 13    # Initial seed
m = 1000   # Modulus
a = 15     # Multiplier
num_samples = 50  # Number of random numbers to generate

# Generate random numbers
random_numbers = multiplicative_congruential_generator(X0, m, a, num_samples)

# Print the generated random numbers
print("Generated random numbers:")
for i, num in enumerate(random_numbers, 1):
    print(f"{i}: {num}")

# Print statistics
print(f"\nStatistics:")
print(f"Minimum value: {min(random_numbers)}")
print(f"Maximum value: {max(random_numbers)}")
print(f"Average value: {sum(random_numbers) / len(random_numbers):.2f}")