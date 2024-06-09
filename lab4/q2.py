# Given data
arrival_rate = 1.0  # in customers per minute
service_rate = 3.0  # in customers per minute (20 seconds per customer)
time_to_seat = 1.5  # in minutes
time_before_game_starts = 2.0  # in minutes

# Calculating total time spent in the system (W) using M/M/1 queue model
W = 1 / (service_rate - arrival_rate)

# Adding the time taken to reach the seat
total_time = W + time_to_seat

# Display the result
print(f"Total time spent by a sports fan to be seated: {total_time:.2f} minutes")

# Check if the fan can expect to be seated before the game starts
if total_time <= time_before_game_starts:
    print("The sports fan can expect to be seated for the kick-off.")
else:
    print("The sports fan cannot expect to be seated for the kick-off.")
