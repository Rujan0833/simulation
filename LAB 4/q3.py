def mm1_queue_measures(arrival_rate, service_rate):
    rho = arrival_rate / service_rate
    L = arrival_rate / (service_rate - arrival_rate)
    Lq = (arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate))
    W = 1 / (service_rate - arrival_rate)
    Wq = arrival_rate / (service_rate * (service_rate - arrival_rate))
    P0 = 1 - rho
    
    return {
        "Utilization (rho)": rho,
        "Average number of customers in system (L)": L,
        "Average number of customers in queue (Lq)": Lq,
        "Average time in system (W)": W,
        "Average time in queue (Wq)": Wq,
        "Probability of zero customers (P0)": P0
    }

arrival_rate = 80.7
service_rate = 38.0

measures = mm1_queue_measures(arrival_rate, service_rate)

for measure, value in measures.items():
    print(f"{measure}: {value:.4f}")
