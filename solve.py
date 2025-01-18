import os
import time
import tracemalloc

def read_words(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def read_word_search(file_path):
    with open(file_path, 'r') as f:
        return [line.strip().split() for line in f]

def preprocess_grid(grid):
    rows = ["".join(row) for row in grid]
    cols = ["".join([grid[row][col] for row in range(len(grid))]) for col in range(len(grid[0]))]
    return rows, cols

def dp_find_word(grid, word, rows, cols):
    for r_idx, row in enumerate(rows):
        start = row.find(word)
        if start != -1:
            return (r_idx, start), (r_idx, start + len(word) - 1)
        start = row.find(word[::-1])
        if start != -1:
            return (r_idx, start + len(word) - 1), (r_idx, start)

    for c_idx, col in enumerate(cols):
        start = col.find(word)
        if start != -1:
            return (start, c_idx), (start + len(word) - 1, c_idx)
        start = col.find(word[::-1])
        if start != -1:
            return (start + len(word) - 1, c_idx), (start, c_idx)

    size = len(grid)
    for r in range(size):
        for c in range(size):
            if r + len(word) <= size and c + len(word) <= size:
                if all(grid[r + i][c + i] == word[i] for i in range(len(word))):
                    return (r, c), (r + len(word) - 1, c + len(word) - 1)
                if all(grid[r + i][c + i] == word[::-1][i] for i in range(len(word))):
                    return (r + len(word) - 1, c + len(word) - 1), (r, c)

            if r - len(word) >= -1 and c + len(word) <= size:
                if all(grid[r - i][c + i] == word[i] for i in range(len(word))):
                    return (r, c), (r - len(word) + 1, c + len(word) - 1)
                if all(grid[r - i][c + i] == word[::-1][i] for i in range(len(word))):
                    return (r - len(word) + 1, c + len(word) - 1), (r, c)

    return None

def dp_solve_wordsearch(grid, words):
    rows, cols = preprocess_grid(grid)
    found_words = {}
    for word in words:
        location = dp_find_word(grid, word, rows, cols)
        if location:
            found_words[word] = location
    return found_words

def find_word_horizontal(grid, word):
    for row in range(len(grid)):
        for col in range(len(grid[0]) - len(word) + 1):
            if grid[row][col:col + len(word)] == list(word):
                return (row, col), (row, col + len(word) - 1)
            if grid[row][col:col + len(word)] == list(word[::-1]):
                return (row, col + len(word) - 1), (row, col)
    return None

def find_word_vertical(grid, word):
    for col in range(len(grid[0])):
        for row in range(len(grid) - len(word) + 1):
            if [grid[row + i][col] for i in range(len(word))] == list(word):
                return (row, col), (row + len(word) - 1, col)
            if [grid[row + i][col] for i in range(len(word))] == list(word[::-1]):
                return (row + len(word) - 1, col), (row, col)
    return None

def find_word_diagonal(grid, word):
    size = len(grid)
    for r in range(size):
        for c in range(size):
            if r + len(word) <= size and c + len(word) <= size:
                if all(grid[r + i][c + i] == word[i] for i in range(len(word))):
                    return (r, c), (r + len(word) - 1, c + len(word) - 1)
                if all(grid[r + i][c + i] == word[::-1][i] for i in range(len(word))):
                    return (r + len(word) - 1, c + len(word) - 1), (r, c)

            if r - len(word) >= -1 and c + len(word) <= size:
                if all(grid[r - i][c + i] == word[i] for i in range(len(word))):
                    return (r, c), (r - len(word) + 1, c + len(word) - 1)
                if all(grid[r - i][c + i] == word[::-1][i] for i in range(len(word))):
                    return (r - len(word) + 1, c + len(word) - 1), (r, c)
    return None

def naive_solve_wordsearch(grid, words):
    found_words = {}
    for word in words:
        location = (
            find_word_horizontal(grid, word) or
            find_word_vertical(grid, word) or
            find_word_diagonal(grid, word)
        )
        if location:
            found_words[word] = location
    return found_words

def print_grid(grid):
    grid_str = "\n".join([" ".join(row) for row in grid])
    return grid_str

def solve_word_search(file_path, word_list_path, algorithm):
    try:
        words = read_words(word_list_path)
        grid = read_word_search(file_path)

        print(f"Solving word search from {file_path} using words from {word_list_path}...\n")

        tracemalloc.start()
        start_time = time.time()

        if algorithm == 'dp':
            found_words = dp_solve_wordsearch(grid, words)
        elif algorithm == 'naive':
            found_words = naive_solve_wordsearch(grid, words)
        else:
            print("Invalid algorithm selection. Choose 'dp' or 'naive'.")
            return

        end_time = time.time()
        memory_used = tracemalloc.get_traced_memory()[1] / 10**6  # Convert to MB
        tracemalloc.stop()

        print("Wordsearch grid:")
        print(print_grid(grid))
        print("\nFound words and locations:")
        for word, location in found_words.items():
            print(f"{word}: {location}")

        print(f"\nTime taken: {end_time - start_time:.4f} seconds")
        print(f"Memory used: {memory_used:.2f} MB")

    except Exception as e:
        print(f"Error solving word search: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the word search file: ")

    print("Available themes:")
    themes = [
        "animals", "body_parts", "clothing", "colors", "countries", "emotions", "food", "fruits",
        "insects", "jobs", "movies", "music", "places", "plants", "school_supplies", "space", "sports",
        "technology", "time", "vehicles", "weather"
    ]
    for theme in themes:
        print(f"- {theme}")
    print("- dictionary (all words from words-alpha.txt)")

    word_list_choice = input("Enter the theme you want to use: ").strip().lower()

    if word_list_choice == "dictionary":
        word_list_path = "words_alpha.txt"
    elif word_list_choice in themes:
        word_list_path = f"words/{word_list_choice}.txt"
    else:
        print("Invalid choice. Exiting.")
        exit()

    print("Choose the algorithm to solve the word search:")
    print("1. Dynamic Programming (dp)")
    print("2. Naive Approach (naive)")
    algorithm_choice = input("Enter 'dp' or 'naive': ").strip().lower()

    solve_word_search(file_path, word_list_path, algorithm_choice)
