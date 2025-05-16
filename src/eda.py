import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Create and save a parallel coordinates plot.
def plot_parallel_coordinates(df, numerical_cols, class_column, save_path=None):
    plt.figure(figsize=(14, 8))
    parallel_coordinates(df[numerical_cols + [class_column]], class_column=class_column, colormap='viridis')
    plt.title('Parallel Coordinates Plot')
    plt.xlabel('Attributes')
    plt.ylabel('Values')
    plt.legend(loc='upper right')
    if save_path:
        plt.savefig(save_path)
    plt.close()