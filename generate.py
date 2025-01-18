import os
import random
import string

def read_words(file_path):
    try:
        with open(file_path, 'r') as f:
            words = [line.strip() for line in f]
            print(f"Read {len(words)} words from {file_path}")
            return words
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
        return []

def create_word_search(words, size=10):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    max_attempts = 1000  # Limit the number of attempts to place each word
    
    for word in words:
        placed = False
        attempts = 0
        while not placed and attempts < max_attempts:
            direction = random.choice(directions)
            start_row = random.randint(0, size - 1)
            start_col = random.randint(0, size - 1)
            end_row = start_row + direction[0] * len(word)
            end_col = start_col + direction[1] * len(word)
            if 0 <= end_row < size and 0 <= end_col < size:
                if all(grid[start_row + i * direction[0]][start_col + i * direction[1]] in (' ', letter) 
                       for i, letter in enumerate(word)):
                    for i, letter in enumerate(word):
                        grid[start_row + i * direction[0]][start_col + i * direction[1]] = letter
                    placed = True
            attempts += 1
        
        if not placed:
            print(f"Failed to place the word '{word}' after {max_attempts} attempts.")
    
    for row in range(size):
        for col in range(size):
            if grid[row][col] == ' ':
                grid[row][col] = random.choice(string.ascii_lowercase)
    
    return grid

def save_word_search(grid, category, num, output_dir):
    try:
        os.makedirs(os.path.join(output_dir, category), exist_ok=True)
        file_path = os.path.join(output_dir, category, f"{category}_{num}.txt")
        with open(file_path, 'w') as f:
            for row in grid:
                f.write(' '.join(row) + '\n')
        print(f"Saved word search to {file_path}")
    except Exception as e:
        print(f"Failed to save {file_path}: {e}")

def generate_word_search(theme, grid_size, output_dir, input_dir, num_files=3):
    try:
        file_path = os.path.join(input_dir, f"{theme}.txt")
        if not os.path.exists(file_path):
            print(f"Theme '{theme}' not found in {input_dir}. Please provide a valid theme.")
            return
        
        words = read_words(file_path)
        for i in range(1, num_files + 1):
            grid = create_word_search(words, size=grid_size)
            save_word_search(grid, theme, i, output_dir)
    except Exception as e:
        print(f"Error generating word searches: {e}")

if __name__ == "__main__":
    input_dir = 'words'
    output_dir = 'generated_word_searches'

    print("Welcome to the Word Search Generator!")
    print("Available themes:")
    available_themes = [file.replace('.txt', '') for file in os.listdir(input_dir) if file.endswith('.txt')]
    for theme in available_themes:
        print(f"- {theme}")
    
    theme = input("Enter the theme you want to use: ").strip()
    if theme not in available_themes:
        print("Invalid theme. Please choose one from the list above.")
        exit(1)
    
    try:
        grid_size = int(input("Enter the grid size (e.g., 10 for 10x10): ").strip())
        num_files = int(input("Enter the number of word searches to generate: ").strip())
        generate_word_search(theme, grid_size, output_dir, input_dir, num_files)
        print(f"Word searches generated in '{output_dir}'!")
    except ValueError:
        print("Invalid input. Please enter numerical values for grid size and number of files.")
