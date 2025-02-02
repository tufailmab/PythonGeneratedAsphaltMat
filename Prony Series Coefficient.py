import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Sample experimental data: (time, relaxation modulus)
# Replace this with your actual data
data = [
    (0.01, 1000), (0.1, 800), (1, 500), (10, 300), (100, 200), (1000, 150)
]

# Convert data to numpy arrays
times = np.array([d[0] for d in data])
moduli = np.array([d[1] for d in data])

# Define the Prony series model with fewer terms
def prony_series(t, G_inf, g1, tau1, g2, tau2):
    return G_inf + g1 * np.exp(-t / tau1) + g2 * np.exp(-t / tau2)

# Initial guess for parameters: G_inf, g1, tau1, g2, tau2
initial_guess = [100, 0.5, 1, 0.3, 10]  # Adjust based on your data

# Perform curve fitting
try:
    params, covariance = curve_fit(prony_series, times, moduli, p0=initial_guess)
except Exception as e:
    print(f"Error during curve fitting: {e}")
    exit()

# Extract parameters
G_inf = params[0]
g1, tau1 = params[1], params[2]
g2, tau2 = params[3], params[4]

# Normalize g_i and k_i so their sums are between 0 and 1
total_g = g1 + g2
total_tau = tau1 + tau2

# Ensure the sum of g_i is between 0 and 1
g1_normalized = g1 / total_g
g2_normalized = g2 / total_g

# Ensure the sum of k_i is between 0 and 1
k1_normalized = tau1 / total_tau
k2_normalized = tau2 / total_tau

# Generate 40 values for each column
gi_list = np.linspace(g1_normalized, g2_normalized, 40)
ki_list = np.linspace(k1_normalized, k2_normalized, 40)
taui_list = np.linspace(tau1, tau2, 40)

# Ensure the sum of g_i and k_i is less than 1
gi_list = gi_list / sum(gi_list)
ki_list = ki_list / sum(ki_list)

# Sort each list independently
sorted_gi = sorted(gi_list)
sorted_ki = sorted(ki_list)
sorted_taui = sorted(taui_list)

# Print results
print(f"G_inf: {G_inf}")
print(f"Prony series coefficients (g_i): {sorted_gi}")
print(f"Relaxation times (tau_i): {sorted_taui}")
print(f"Normalized k_i: {sorted_ki}")

# Define the density value
density_value = 2.4e-09

# Write results to an .inp file with the correct ABAQUS format
output_file = "Python Generated Asphalt Material.inp"
with open(output_file, "w") as f:
    f.write("** MATERIALS\n")
    f.write("** \n")
    f.write("** Developer:\n")
    f.write("** Engr. Tufail Mabood\n")
    f.write("** WhatsApp:\n")
    f.write("** https://wa.me/+923440907874\n")
    f.write("** Note:\n")
    f.write("** If you are a researcher or developer and want to make modifications, my code \n")
    f.write("** is open source. Feel free to make changes and cite this tool as well.\n")
    f.write("*Material, name=\"Python Generated Asphalt Mat\"\n")
    f.write("*Density\n")
    f.write(f" {density_value},\n")  # Write the density value
    f.write("*Viscoelastic, time=PRONY\n")
    
    # Write PRONY series values with correct ABAQUS float formatting
    for g, k, tau in zip(sorted_gi, sorted_ki, sorted_taui):
        # Ensure all values are floats and formatted correctly
        f.write(f" {g:.6f}, {k:.6f}, {tau:.6f}\n")  # Write values with 6 decimal places as floats

print(f"Results written to {output_file}")

# Print a message to remind the user to define the stress relaxation data if required
print("Note: If you need to define stress relaxation data, please ensure to include it in the input file.")

# Plot the results
plt.scatter(times, moduli, label='Experimental Data')
plt.plot(times, prony_series(times, *params), label='Prony Series Fit', color='red')
plt.xlabel('Time (s)')
plt.ylabel('Relaxation Modulus')
plt.legend()
plt.show()
