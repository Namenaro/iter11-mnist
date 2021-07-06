import operator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_points_on_pic(pic, X,Y, colors=None):
    if colors is None:
        colors = 'green'
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    plt.scatter(X[0], Y[0], s=100, c='red', marker='o', alpha=0.4)
    plt.scatter(X[1:], Y[1:], s=100, c=colors, marker='o', alpha=0.4)
    return fig

def plot_several_graphs(graphs, names):
    fig, axs = plt.subplots(len(graphs))
    for i in range(len(graphs)):
        axs[i].plot(graphs[i])
        axs[i].set_title(names[i])
    return fig

def plot_several_lines_pics_with_one_colorbar(pics_series):
    rows = len(pics_series)
    num_pics_in_seria = len(pics_series[0])
    fig, axs = plt.subplots(rows, num_pics_in_seria)
    MIN, MAX = np.array(pics_series).min(), np.array(pics_series).max()
    for row in range(rows):
        for col in range(num_pics_in_seria):
            im = axs[row, col].imshow(pics_series[row][col], cmap='Blues', vmin=MIN, vmax=MAX)

    fig.colorbar(im, ax=axs.ravel().tolist())
    return fig

def plot_several_pics_with_one_colorbar(pics):
    num_pics_in_seria = len(pics)
    fig, axs = plt.subplots(num_pics_in_seria)
    MIN, MAX = np.array(pics).min(), np.array(pics).max()

    for i in range(num_pics_in_seria):
        im = axs[i].imshow(pics[i], cmap='Blues', vmin=MIN, vmax=MAX)

    fig.colorbar(im, ax=axs.ravel().tolist())
    return fig

def plot_hist(values, nbins=15):
    plt.clf()
    fig, ax = plt.subplots()
    values = np.array(values).flatten()
    (probs, bins, _) = plt.hist(values, bins=nbins,
                                weights=np.ones_like(values) / len(values), range=(0, values.max()))
    return fig