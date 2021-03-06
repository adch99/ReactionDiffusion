# All video making functionality
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import ArtistAnimation
import os
import glob
import subprocess

def saveVideo(filename="output.mp4", fps=10):
    command = r"ffmpeg -r " + str(fps) + " -i img/%03d.png -vcodec mpeg4 -acodec aac " + filename + " -v quiet -y"
    exit_code = subprocess.call(command, shell=True)

    if exit_code != 0:
        print("Encountered error in ffmpeg! Running again in verbose mode.")
        process_return = subprocess.call(r"ffmpeg -r " + str(fps) + " -i img/%03d.png -vcodec mpeg4 -acodec aac " + filename + " -y", shell=True)


def makeVideo(snapshots, **config):
    # First clean up the img directory
    to_remove = glob.glob("./img/*.png")
    for path in to_remove:
        os.remove(path)
    getImages(snapshots)

def getImages(snapshots):
    max_conc = np.amax(np.array([snap.max() for snap in snapshots]))
    norm = mpl.colors.LogNorm(vmax=max_conc)
    cmap = mpl.cm.Blues
    mappable = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    num_reagents = snapshots[0].shape[0]

    counter = 1
    for snap in snapshots:
        fig, ax = plt.subplots(nrows=(num_reagents+1)//2, ncols=2, figsize=(10,10))
        ax = ax.flatten()
        for reagent in range(num_reagents):
            ax[reagent].set_title("Reagent %d" % reagent)
            axis_artist = ax[reagent].imshow(snap[reagent, :, :],
                cmap=cmap,
                norm=norm,
                animated=True)
        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        cbar = fig.colorbar(mappable, cax=cbar_ax)
        fig.savefig("img/%03d.png" % counter)
        plt.close()
        counter += 1