import pandas as pd
import os

def merge_csv_files(input_dir, output_file):
    all_data = []

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_dir, file_name)
            grid_size = file_name.split('_')[3]
            print(grid_size)
              # Extract grid size from file name (e.g., "10_100")
            
            # Load CSV and add grid size column
            data = pd.read_csv(file_path)
            data['grid_size'] = grid_size
            all_data.append(data)
    
    # Combine all data
    merged_data = pd.concat(all_data, ignore_index=True)
    merged_data.to_csv(output_file, index=False)
    print(f"Merged data saved to {output_file}")

if __name__ == "__main__":
    input_dir = "results"  # Folder containing individual CSVs
    output_file = "merged_results.csv"
    merge_csv_files(input_dir, output_file)
