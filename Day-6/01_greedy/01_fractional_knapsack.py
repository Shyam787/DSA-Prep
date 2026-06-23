def fractional_knapsack(values, weights, capacity):
    n = len(values)

    # build list
    items = []
    for i in range(n):
        if weights[i] == 0:
            continue

        ratio = values[i]/weights[i]
        items.append((ratio, values[i], weights[i]))
    
    # sort by ratio
    items.sort(key = lambda x : x[0], reverse = True)

    total_value = 0.0

    for ratio, value, weight in items:
        
        if capacity <= 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight

        else:
            total_value += ratio * capacity
            capacity = 0
        
    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Test Case 1 Output:", fractional_knapsack(values, weights, capacity))
# Expected: 240.0

# Test Case 2
values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]
capacity = 10

print("Test Case 2 Output:", fractional_knapsack(values, weights, capacity))
# Expected output: 105.0

# Test Case 3 (edge case: zero capacity)
values = [100, 200, 300]
weights = [10, 20, 30]
capacity = 0

print("Test Case 3 Output:", fractional_knapsack(values, weights, capacity))
# Expected: 0.0         