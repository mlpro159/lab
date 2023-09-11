from constraint import Problem

# Define the regions and their neighbors
regions = ['Telangana', 'Karnataka', 'Tamil Nadu', 'Kerala']
neighbors = {
    'Telangana': ['Karnataka', 'Tamil Nadu'],
    'Karnataka': ['Telangana', 'Tamil Nadu', 'Kerala'],
    'Tamil Nadu': ['Telangana', 'Karnataka', 'Kerala'],
    'Kerala': ['Karnataka', 'Tamil Nadu']
}

# Define the colors
colors = ["Red", "Green", "Blue"]

# Create a CSP problem instance
problem = Problem()

# Add variables for each region with possible color choices
for region in regions:
    problem.addVariable(region, colors)

# Define the constraints (no adjacent regions can have the same color)
for region, neighbor_list in neighbors.items():
    for neighbor in neighbor_list:
        problem.addConstraint(lambda color1, color2: color1 != color2, (region, neighbor))

# Find a solution to the CSP problem
solutions = problem.getSolutions()

if len(solutions) > 0:
    solution = solutions[0]  # Choose the first solution

    # Print the coloring result
    print("Map Coloring Result:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")
