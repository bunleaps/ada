import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(data_file):
    # Load the CSV file
    df = pd.read_csv(data_file)
    
    # Ensure grid_size is treated as integers
    df['grid_size'] = df['grid_size'].astype(int)
    
    # Create a new DataFrame for average time and memory usage by grid size and algorithm
    df_melted = pd.melt(
        df,
        id_vars=['category', 'file', 'grid_size'],
        value_vars=['dp_time', 'naive_time'],
        var_name='algorithm',
        value_name='avg_time'
    )
    
    # Clean algorithm names
    df_melted['algorithm'] = df_melted['algorithm'].str.replace('_time', '').str.capitalize()

    # Plot Time Complexity
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_melted, x="grid_size", y="avg_time", hue="algorithm", marker="o")
    plt.title("Time Complexity vs Grid Size")
    plt.xlabel("Grid Size")
    plt.ylabel("Average Time (s)")
    plt.legend(title="Algorithm")
    plt.grid()
    plt.savefig("time_complexity.png")
    plt.show()

    # Create a new DataFrame for comparisons
    df_comparisons = pd.melt(
        df,
        id_vars=['category', 'file', 'grid_size'],
        value_vars=['dp_comparisons', 'naive_comparisons'],
        var_name='algorithm',
        value_name='comparisons'
    )
    
    # Clean algorithm names
    df_comparisons['algorithm'] = df_comparisons['algorithm'].str.replace('_comparisons', '').str.capitalize()

    # Plot Comparisons
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_comparisons, x="grid_size", y="comparisons", hue="algorithm")
    plt.title("Steps vs Grid Size")
    plt.xlabel("Grid Size")
    plt.ylabel("Number of Steps")
    plt.legend(title="Algorithm")
    plt.grid()
    plt.savefig("comparisons.png")
    plt.show()

if __name__ == "__main__":
    data_file = "merged_results.csv"
    plot_data(data_file)
