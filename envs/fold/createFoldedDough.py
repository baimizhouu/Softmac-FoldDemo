import numpy as np

# Define the properties of the semi-cylindrical dough
h = 0.01  # height of the semi-cylinder along the Y-axis (vertical)
r = 0.16  # radius of the semi-cylinder
init_pos = np.array([0.5, 0., 0.5])  # initial position of the semi-cylinder's center
n_particles = 3000  # number of particles in the vertex cloud

# Function to generate points within a semi-cylindrical volume with Y-axis as vertical
def generate_semi_cylinder_points(h, r, init_pos, n_particles):
    points = []
    for _ in range(n_particles):
        theta = np.random.uniform(0, np.pi)  # Generating points only in semi-circle for semi-cylinder
        y = np.random.uniform(0, h * 2)  # Height variation along Y-axis
        radius = np.sqrt(np.random.uniform(0, r**2))  # Ensure uniform distribution within the circle
        x = radius * np.cos(theta)
        z = radius * np.sin(theta)
        
        # Apply initial position offset
        point = np.array([x, y, z]) + init_pos
        points.append(point)
        
    return np.array(points)

# Generate the vertex cloud for the semi-cylindrical dough
vertex_cloud = generate_semi_cylinder_points(h, r, init_pos, n_particles)

# Save the vertex cloud to a .npy file
file_path = 'folded_dough.npy'
np.save(file_path, vertex_cloud)

print(f"Vertex cloud saved to {file_path}")
