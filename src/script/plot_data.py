import matplotlib.pylab as plt
import numpy as np

def plot_data(data, figsize=(16, 4)):
    fig, axes = plt.subplots(1, 1, figsize=figsize)
    axes.imshow(data[0].T, aspect='auto', origin='lower', 
                    interpolation='none')
    fig.savefig(f'output_ppg/alignment_plot.png')

plot_data(np.load("alignment.npy"))