import numpy as np
import math

# Cylinder properties adjusted for lying on x-z plane
h = 0.01  # height (along y-axis now, representing the thickness of the dough)
r = 0.16  # radius
init_pos = (0.5, 0., 0.5)  # initial position (adjusted to lie on x-z plane)
n_particles = 3000  # number of particles

# Generate points within the cylinder lying on x-z plane
points = []
while len(points) < n_particles:
    theta = np.random.uniform(0, 2*np.pi)  # Angle for circular base
    rad = np.random.uniform(0, r)  # Random radius within the cylinder's radius
    x = rad * math.cos(theta)  # x-coordinate based on radius and angle
    z = rad * math.sin(theta)  # z-coordinate based on radius and angle
    y = np.random.uniform(0, h)  # y-coordinate (height/thickness) uniformly distributed
    points.append((x + init_pos[0], y + init_pos[1], z + init_pos[2]))  # Append adjusted point

# Convert to numpy array
points_np = np.array(points)

# Specify your local file path to save the npy file
local_file_path = 'dough.npy'
np.save(local_file_path, points_np)

print(f"Points saved to {local_file_path}")
