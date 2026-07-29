import numpy as np
import matplotlib.pyplot as plt

# URL of the dataset
file = "./Data/ch180.csv"

# Load data
# Skip comment lines starting with #
data = np.loadtxt(file, comments='#')

# Extract first and third columns
x = data[:, 0]
y = data[:, 2]

# Create plot
plt.figure(figsize=(7,5))
plt.plot(x, y, linewidth=2)

# Labels and title
plt.xlabel('Y')
plt.ylabel('U')
plt.title('Channel Flow Data: Re 180')

# Grid
plt.grid(True)

# Show plot
plt.show()

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

