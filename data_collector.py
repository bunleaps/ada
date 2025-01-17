import os
import csv
# import tracemalloc
import time
from word_search_solver import dp_solve_wordsearch, naive_solve_wordsearch, read_words, read_word_search

def solve_word_searches(input_dir, output_csv):
    results = []

    for category in os.listdir(input_dir):
        category_path = os.path.join(input_dir, category)
        if os.path.isdir(category_path):
            for file_name in os.listdir(category_path):
                if file_name.endswith('.txt'):
                    grid_file = os.path.join(category_path, file_name)
                    word_list = read_words(os.path.join('words', f"{category}.txt"))
                    wordsearch_grid = read_word_search(grid_file)

                    # Dynamic Programming Solution
                    dp_start_time = time.time()
                    dp_found, dp_comparisons = dp_solve_wordsearch(wordsearch_grid, word_list)
                    dp_duration = time.time() - dp_start_time

                    # Naive Solution
                    naive_start_time = time.time()
                    naive_found, naive_comparisons = naive_solve_wordsearch(wordsearch_grid, word_list)
                    naive_duration = time.time() - naive_start_time

                    # Collect data
                    results.append({
                        'category': category,
                        'file': file_name,
                        'grid_size': f"{len(wordsearch_grid)}x{len(wordsearch_grid[0])}",
                        'dp_time': dp_duration,
                        'dp_comparisons': dp_comparisons,
                        'naive_time': naive_duration,
                        'naive_comparisons': naive_comparisons
                    })

    # Save results to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['category', 'file', 'grid_size', 'dp_time', 'dp_comparisons', 'naive_time', 'naive_comparisons']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

    print(f"Results saved to {output_csv}")
