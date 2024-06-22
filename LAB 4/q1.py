# Given data
mean_inter_arrival_time = 10.0  # in minutes
mean_service_time = 5.0  # in minutes

# Calculating arrival rate (lambda) and service rate (mu)
lambda_rate = 1.0 / mean_inter_arrival_time
mu_rate = 1.0 / mean_service_time

# a. Probability that a customer will not have to wait at the counter
P0 = 1 - (lambda_rate / mu_rate)

# b. Expected number of customers in the bank
L = lambda_rate / (mu_rate - lambda_rate)

# c. Time a customer expects to spend in the bank
W = 1 / (mu_rate - lambda_rate)

# Display the results
print(f"Probability that a customer will not have to wait at the counter (P0): {P0:.2f}")
print(f"Expected number of customers in the bank (L): {L:.2f}")
print(f"Time a customer expects to spend in the bank (W): {W:.2f} minutes")
