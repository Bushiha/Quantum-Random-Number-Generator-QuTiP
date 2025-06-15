
# Quantum Random Number Generator using QuTiP

from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# Create basis states |0> and |1>
zero = basis(2, 0)
one = basis(2, 1)

# Apply Hadamard gate (superposition)
H = hadamard_transform(1)
psi = H * zero

# Measurement probabilities
prob_0 = abs((zero.dag() * psi)[0][0]) ** 2
prob_1 = abs((one.dag() * psi)[0][0]) ** 2

print(f"Probability of 0: {prob_0}")
print(f"Probability of 1: {prob_1}")

# Simulate 1000 measurements
outcomes = np.random.choice([0, 1], size=1000, p=[prob_0, prob_1])

# Count occurrences
counts = {0: np.count_nonzero(outcomes == 0),
          1: np.count_nonzero(outcomes == 1)}

print(f"Measurement outcomes over 1000 shots: {counts}")

# Plot histogram
plt.bar(counts.keys(), counts.values(), tick_label=['0', '1'], color=['blue', 'green'])
plt.title("Quantum Random Number Generator (QuTiP)")
plt.xlabel("Outcome")
plt.ylabel("Counts")
plt.show()
