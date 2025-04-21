import numpy as np
import matplotlib.pyplot as plt

def logistic_map(x, r):
    """Logistic map function"""
    return r * x * (1 - x)

def generate_bifurcation_diagram(r_values, iterations=1000, last=100):
    """
    Generate the bifurcation diagram for the logistic map.
    
    Parameters:
    - r_values: array of r parameter values
    - iterations: number of iterations to run for each r
    - last: number of last iterations to plot for each r
    
    Returns:
    - Tuple of (r_values, x_values) for plotting
    """
    x = 1e-5 * np.ones(len(r_values))  # Initial condition
    bifurcation_data = []
    
    for _ in range(iterations):
        x = logistic_map(x, r_values)
        
        # We only plot the last 'last' iterations to see the attractor
        if _ >= (iterations - last):
            bifurcation_data.append((r_values, x))
    
    return bifurcation_data

# Parameters
r_min, r_max = 2.5, 4.0  # Range of r values to explore. Interesting > 3.
num_r = 1000             # Number of r values to sample
iterations = 5000        # Number of iterations per r
last = 200              # Number of last iterations to plot

# Generate r values
r_values = np.linspace(r_min, r_max, num_r)

# Generate bifurcation data
bifurcation_data = generate_bifurcation_diagram(r_values, iterations, last)

# Plotting
plt.figure(figsize=(12, 8))
for r, x in bifurcation_data:
    plt.plot(r, x, '.k', markersize=1.0, alpha=0.5)

plt.title('Bifurcation Diagram of the Logistic Map', fontsize=16)
plt.xlabel('Growth rate (r)', fontsize=14)
plt.ylabel('Population (x)', fontsize=14)
plt.xlim(r_min, r_max)
plt.grid(alpha=0.3)
plt.show()
