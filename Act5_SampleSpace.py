#Creating 3d20 tuples
all_tuples = []
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            all_tuples.append((i, j, k))

from collections import defaultdict
import matplotlib.pyplot as plt

# Dictionary to store the frequency of each sum
tuple_dist = defaultdict(int)

# Compute sums and count occurrences
for res in all_tuples:
    total_sum = sum(res)
    tuple_dist[total_sum] += 1

# Converting to regular dictionary for easier computations
tuple_dist = dict(tuple_dist)

# Creating new dictionary with probabilities for each sum value
total_outcomes = len(all_tuples)  # Should be 8000
probabilities = {k: v / total_outcomes for k, v in tuple_dist.items()}

# Should be sorted but sorting anyways
x_vals = sorted(probabilities.keys())  # X-axis: possible sums
y_vals = [probabilities[x] for x in x_vals]  # Y-axis: probability of each sum

# Plot the probability distribution
plt.figure(figsize=(10, 5))
plt.bar(x_vals, y_vals, color='blue', alpha=0.7, edgecolor='black')

plt.xlabel("Sum of Three 20-Sided Dice")
plt.ylabel("Probability")
plt.title("Probability Distribution of the Sum of Three 20-Sided Dice")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()