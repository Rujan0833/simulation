# WAP to solve the below Weather problem
# Rainy today => 40% Rainy tomorrow
#              => 60% not Rainy tomorrow
# Not rainy today => 20% Rainy tomorrow
#               => 80% not Rainy tomorrow
# What will be probability if todays is not raining then not rain the day after tomorrow?


def weather_probability():
    # Define the transition probabilities
    rainy_to_rainy = 0.4
    rainy_to_not_rainy = 0.6
    not_rainy_to_rainy = 0.2
    not_rainy_to_not_rainy = 0.8

    # Step 1: Probability of not raining tomorrow given it's not raining today
    prob_not_rain_tomorrow = not_rainy_to_not_rainy

    # Step 2: Probability of not raining the day after tomorrow
    # We need to consider both possibilities for tomorrow's weather
    prob_not_rain_day_after = (
        prob_not_rain_tomorrow * not_rainy_to_not_rainy +  # If it doesn't rain tomorrow
        (1 - prob_not_rain_tomorrow) * rainy_to_not_rainy  # If it rains tomorrow
    )

    return prob_not_rain_day_after

# Calculate the probability
result = weather_probability()

print(f"The probability that it will not rain the day after tomorrow, given that it's not raining today, is: {result:.4f}")
print(f"This is equivalent to {result*100:.2f}%")