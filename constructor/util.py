import io

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image as IPImage
from IPython.display import display
from PIL import Image, ImageDraw


# Function to visualize the grid and store the image in memory
def save_grid_image_to_memory(grid):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(-0.5, len(grid), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(grid[0]), 1), minor=True)
    ax.grid(which="minor", color="black", linestyle="-", linewidth=2)
    ax.tick_params(which="minor", size=0)

    # Create a numpy array to store the grid state for visualization
    image_data = np.zeros((len(grid), len(grid[0])))

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            image_data[i, j] = 1 if cell.state == "alive" else 0

    ax.imshow(image_data, cmap="gray", interpolation="nearest")
    # Save the figure to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return Image.open(buf)


# Function to create a GIF in memory and display it in the notebook
def create_gif_in_memory(images, duration=500):
    buf = io.BytesIO()
    images[0].save(
        buf,
        format="GIF",
        save_all=True,
        append_images=images[1:],
        loop=0,
        duration=duration,
    )
    buf.seek(0)
    return buf


# Function to display the GIF in the notebook
def display_gif_in_notebook(gif_data):
    display(IPImage(data=gif_data.read(), format="gif"))
