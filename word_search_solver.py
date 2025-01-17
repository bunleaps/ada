

# Global counters for comparisons
dp_comparisons = 0
naive_comparisons = 0

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
    global dp_comparisons
    for r_idx, row in enumerate(rows):
        dp_comparisons += len(row)
        start = row.find(word)
        if start != -1:
            return (r_idx, start), (r_idx, start + len(word) - 1)
        start = row.find(word[::-1])
        if start != -1:
            return (r_idx, start + len(word) - 1), (r_idx, start)

    for c_idx, col in enumerate(cols):
        dp_comparisons += len(col)
        start = col.find(word)
        if start != -1:
            return (start, c_idx), (start + len(word) - 1, c_idx)
        start = col.find(word[::-1])
        if start != -1:
            return (start + len(word) - 1, c_idx), (start, c_idx)

    # Diagonal search
    size = len(grid)
    for r in range(size):
        for c in range(size):
            # Top-left to bottom-right
            if r + len(word) <= size and c + len(word) <= size:
                dp_comparisons += len(word)
                if all(grid[r + i][c + i] == word[i] for i in range(len(word))):
                    return (r, c), (r + len(word) - 1, c + len(word) - 1)
                if all(grid[r + i][c + i] == word[::-1][i] for i in range(len(word))):
                    return (r + len(word) - 1, c + len(word) - 1), (r, c)

            # Bottom-left to top-right
            if r - len(word) >= -1 and c + len(word) <= size:
                dp_comparisons += len(word)
                if all(grid[r - i][c + i] == word[i] for i in range(len(word))):
                    return (r, c), (r - len(word) + 1, c + len(word) - 1)
                if all(grid[r - i][c + i] == word[::-1][i] for i in range(len(word))):
                    return (r - len(word) + 1, c + len(word) - 1), (r, c)

    return None


def dp_solve_wordsearch(grid, words):
    global dp_comparisons
    dp_comparisons = 0  # Reset comparisons counter
    rows, cols = preprocess_grid(grid)
    found_words = {}
    for word in words:
        location = dp_find_word(grid, word, rows, cols)
        if location:
            found_words[word] = location
    return found_words, dp_comparisons

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
            # Top-left to bottom-right
            if r + len(word) <= size and c + len(word) <= size:
                if all(grid[r + i][c + i] == word[i] for i in range(len(word))):
                    return (r, c), (r + len(word) - 1, c + len(word) - 1)
                if all(grid[r + i][c + i] == word[::-1][i] for i in range(len(word))):
                    return (r + len(word) - 1, c + len(word) - 1), (r, c)
            
            # Bottom-left to top-right
            if r - len(word) >= -1 and c + len(word) <= size:
                if all(grid[r - i][c + i] == word[i] for i in range(len(word))):
                    return (r, c), (r - len(word) + 1, c + len(word) - 1)
                if all(grid[r - i][c + i] == word[::-1][i] for i in range(len(word))):
                    return (r - len(word) + 1, c + len(word) - 1), (r, c)
    return None

def naive_solve_wordsearch(grid, words):
    global naive_comparisons
    naive_comparisons = 0  # Reset comparisons counter
    found_words = {}
    for word in words:
        for row in grid:
            naive_comparisons += len(row)
        location = (
            find_word_horizontal(grid, word) or
            find_word_vertical(grid, word) or
            find_word_diagonal(grid, word)
        )
        if location:
            found_words[word] = location
    return found_words, naive_comparisons
