import os
import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Initialize data storage
folders = [f"word_search_{i}_100" for i in range(10, 101, 10)]
all_data = []

# Parse data from each folder's summary.txt
for folder in folders:
    summary_path = os.path.join(folder, "summary.txt")
    if os.path.exists(summary_path):
        with open(summary_path, "r") as file:
            content = file.read()
            matches = re.findall(
                r"Category: (.+?)\nDP Average Time: ([\d.]+) seconds\nDP Average Memory: [\d.]+ MB\nNaive Average Time: ([\d.]+) seconds",
                content,
            )
            for match in matches:
                all_data.append({
                    "folder": folder,
                    "category": match[0],
                    "dp_time": float(match[1]),
                    "naive_time": float(match[2]),
                })

# Convert to DataFrame
df = pd.DataFrame(all_data)

### Line Plot for Trends ###
plt.figure(figsize=(16, 10))

for folder in folders:
    subset = df[df["folder"] == folder]
    plt.plot(
        subset["category"],
        subset["dp_time"],
        marker="o",
        label=f"DP Time ({folder})"
    )
    plt.plot(
        subset["category"],
        subset["naive_time"],
        marker="x",
        linestyle="--",
        label=f"Naive Time ({folder})"
    )

# Add labels and legend
plt.xticks(rotation=45, ha="right")
plt.ylabel("Time (seconds)")
plt.title("Comparison of DP and Naive Times Across Folders and Categories")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Show the plot
plt.show()

### Heatmap for Compact View ###
# Pivot DataFrame for heatmap
dp_pivot = df.pivot(index="category", columns="folder", values="dp_time")
naive_pivot = df.pivot(index="category", columns="folder", values="naive_time")

# Plot DP times heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(dp_pivot, annot=True, fmt=".4f", cmap="Blues")
plt.title("DP Average Times (seconds)")
plt.ylabel("Category")
plt.xlabel("Folder")
plt.tight_layout()
plt.show()

# Plot Naive times heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(naive_pivot, annot=True, fmt=".4f", cmap="Reds")
plt.title("Naive Average Times (seconds)")
plt.ylabel("Category")
plt.xlabel("Folder")
plt.tight_layout()
plt.show()
