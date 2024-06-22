import random

def simulate_mm1_queue(arrival_rate, service_rate, max_time):
    random.seed(42)  # For reproducibility

    time = 0
    num_customers = 0
    total_customers = 0
    total_waiting_time = 0
    total_system_time = 0
    max_customers_in_system = 0

    arrival_times = []
    service_times = []

    while time < max_time:
        if num_customers == 0:
            next_arrival_time = random.expovariate(arrival_rate)
            next_service_time = next_arrival_time + random.expovariate(service_rate)
        else:
            next_arrival_time = time + random.expovariate(arrival_rate)
            next_service_time = time + random.expovariate(service_rate)
        
        if next_arrival_time < next_service_time:
            time = next_arrival_time
            num_customers += 1
            arrival_times.append(time)
        else:
            time = next_service_time
            num_customers -= 1
            if arrival_times:
                arrival_time = arrival_times.pop(0)
                waiting_time = time - arrival_time
                total_waiting_time += waiting_time
                total_system_time += waiting_time + random.expovariate(service_rate)
        
        total_customers += 1
        max_customers_in_system = max(max_customers_in_system, num_customers)
    
    rho = arrival_rate / service_rate
    avg_customers_in_system = total_system_time / max_time
    avg_customers_in_queue = (total_system_time - total_customers * (1 / service_rate)) / max_time
    avg_time_in_system = total_system_time / total_customers
    avg_time_in_queue = total_waiting_time / total_customers
    prob_zero_customers = 1 - rho

    return {
        "Utilization (rho)": rho,
        "Average number of customers in system (L)": avg_customers_in_system,
        "Average number of customers in queue (Lq)": avg_customers_in_queue,
        "Average time in system (W)": avg_time_in_system,
        "Average time in queue (Wq)": avg_time_in_queue,
        "Probability of zero customers (P0)": prob_zero_customers,
        "Max customers in system": max_customers_in_system
    }

arrival_rate = 1.0
service_rate = 3.0
max_time = 10000  # Simulation time in minutes

measures = simulate_mm1_queue(arrival_rate, service_rate, max_time)

for measure, value in measures.items():
    print(f"{measure}: {value:.4f}")
