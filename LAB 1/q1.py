Y_prev = 80
G_values = [20, 25, 30, 35, 40]
results = []
previous_consumption = None

for year, G in enumerate(G_values, start=1):
    I = 2 + 0.1 * Y_prev
    Y = 45.45 + 2.27 * (I + G)
    T = 0.2 * Y
    C = 20 + 0.7 * (Y - T)
    
    if previous_consumption is not None:
        growth = ((C - previous_consumption) / previous_consumption) * 100
    else:
        growth = 0  # Assume growth is zero for the first year
    
    results.append((year, G, Y, T, C, growth))
    
    Y_prev = Y
    previous_consumption = C

header = f"{'Year':<5} {'Gov Exp':<10} {'Income':<10} {'Taxes':<10} {'Consumption':<15} {'Growth (%)':<10}"
print(header)
print("=" * len(header))
for year, G, Y, T, C, growth in results:
    growth_str = f"{growth:.2f}%" if growth is not None else "N/A"
    print(f"{year:<5} {G:<10} {Y:<10.2f} {T:<10.2f} {C:<15.2f} {growth_str:<10}")

#hello