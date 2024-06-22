arrival_rate = 1.0  # in customers per minute
service_rate = 3.0  # in customers per minute
time_to_seat = 1.5  # in minutes
time_before_game_starts = 2.0  # in minutes

W = 1 / (service_rate - arrival_rate)
total_time = W + time_to_seat

print(f"Total time spent by a sports fan to be seated: {total_time:.2f} minutes")

if total_time <= time_before_game_starts:
    print("The sports fan can expect to be seated for the kick-off.")
else:
    print("The sports fan cannot expect to be seated for the kick-off.")
