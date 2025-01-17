import pandas as pd
import matplotlib.pyplot as plt

def plot_comparisons(data_csv):
    data = pd.read_csv(data_csv)

    # Plot comparisons
    grid_sizes = data['grid_size'].unique()
    dp_comparisons = data.groupby('grid_size')['dp_comparisons'].mean()
    naive_comparisons = data.groupby('grid_size')['naive_comparisons'].mean()

    plt.plot(grid_sizes, dp_comparisons, label='Dynamic Programming')
    plt.plot(grid_sizes, naive_comparisons, label='Naive Method')
    plt.xlabel('Grid Size')
    plt.ylabel('Number of Comparisons')
    plt.title('Grid Size vs. Number of Comparisons')
    plt.legend()
    plt.grid()
    plt.show()

def plot_times(data_csv):
    data = pd.read_csv(data_csv)

    # Plot runtime
    grid_sizes = data['grid_size'].unique()
    dp_time = data.groupby('grid_size')['dp_time'].mean()
    naive_time = data.groupby('grid_size')['naive_time'].mean()

    plt.plot(grid_sizes, dp_time, label='Dynamic Programming')
    plt.plot(grid_sizes, naive_time, label='Naive Method')
    plt.xlabel('Grid Size')
    plt.ylabel('Time (s)')
    plt.title('Grid Size vs. Runtime')
    plt.legend()
    plt.grid()
    plt.show()
