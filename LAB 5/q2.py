# Coke - Pepsi
# Coke => 90% Coke
# Pepsi => 20% Coke
# Given a person is currently a Pepsi purchaser. What is the probability of purchase of coke after two purchases from now?
# WAP to solve the above problem.

# Define the transition matrix
P = [
    [0.9, 0.1],
    [0.2, 0.8]
]

# Initial state vector (currently a Pepsi purchaser)
v0 = [0, 1]

# Function to multiply two matrices
def matrix_multiply(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Function to multiply matrix and vector
def vector_multiply(matrix, vector):
    result = [0, 0]
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

# Calculate P^2
P2 = matrix_multiply(P, P)

# Calculate the state vector after two transitions
v2 = vector_multiply(P2, v0)

# Probability of purchasing Coke after two purchases
prob_coke_after_two_purchases = v2[0]

print("Probability of purchasing Coke after two purchases:", prob_coke_after_two_purchases)
