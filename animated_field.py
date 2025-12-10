import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.colors import ListedColormap
import numpy as np

from conway_config import USE_NUMPY, INTERVAL_FOR_ANI


def animate_history(history):
    fig, ax = plt.subplots(figsize=(10, 10))
    cmap = ListedColormap(['black', 'white'])

    if USE_NUMPY:
        first_frame = history[0]
    else:
        first_frame = np.array(history[0])

    im = ax.imshow(first_frame, cmap=cmap)
    ax.axis("off")

    def update(frame_num):
        if USE_NUMPY:
            frame = history[frame_num]
        else:
            frame = np.array(history[frame_num])
    
        im.set_array(frame)
        return [im]
    
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(history),
        interval=INTERVAL_FOR_ANI,
        blit=True
    )
    plt.show()