# Word Search Solver App

The Word Search Solver App is designed to help users create or solve word search puzzles effortlessly. Follow the instructions below to get started.

---

## **Features**

- Generate word search puzzles with customizable themes, grid sizes, and word counts.
- Solve existing word search puzzles using efficient algorithms.
- Analyze performance with metrics like time taken and memory used.

---

## **For Users Without an Existing Word Search Puzzle**

If you don’t already have a word search puzzle, you can generate one using the `generate.py` script.

### **Steps to Generate a Word Search**

1. **Locate and Run the Script**

   - Open your terminal or command prompt.
   - Navigate to the folder containing the `generate.py` file.
   - Run the script by typing:
     ```
     python generate.py
     ```

2. **Answer the Prompts**

   - **Choose a Theme**: Enter a theme for your word search (e.g., `animals`, `space`).
   - **Specify Grid Size**: Enter the desired grid size (e.g., 15 for a 15x15 grid).
   - **Select the Number of Words**: Specify how many words you want in the puzzle.

3. **Save the Generated Puzzle**

   - The script will display the generated word search and save it as a text file in the same folder as the script.
   - Open the saved text file to view or share the puzzle.

---

## **For Users with an Existing Word Search Puzzle**

If you already have a word search puzzle, ensure it is saved in a `.txt` file and formatted correctly.

### **Word Search File Format**

- Each row of letters must be on a separate line.
- Letters must be separated by spaces.
- Example:
  ```
  q x z j k y u b x e l e p h a n t f f c
  f y y f w h a l e i s g o r c s d s t r
  q k u b n f d m t m u l e c o e k e a o
  ```

### **Steps to Solve a Word Search**

1. **Launch the Solver Script**

   - Open your terminal or command prompt.
   - Navigate to the folder containing the solver script.
   - Run the script by typing:
     ```
     python solve.py
     ```

2. **Provide the Word Search File Path**

   - Enter the path to your word search file when prompted. Example:
     ```
     Enter the path to the word search file: generated_word_searches\space\space_1.txt
     ```

3. **Select a Theme**

   - Choose a theme that matches the words in your word search. Available themes include:
     - `animals`
     - `body_parts`
     - `clothing`
     - `colors`
     - `countries`
     - `emotions`
     - `food`
     - `fruits`
     - `insects`
     - `jobs`
     - `movies`
     - `music`
     - `places`
     - `plants`
     - `school_supplies`
     - `space`
     - `sports`
     - `technology`
     - `time`
     - `vehicles`
     - `weather`
     - `dictionary` (all words from `words-alpha.txt`)

4. **Choose a Solving Algorithm**

   - The app supports two algorithms:
     1. **Dynamic Programming (dp)**: Optimized for larger puzzles.
     2. **Naive Approach (naive)**: Simple but slower for larger puzzles.
   - Enter `dp` or `naive` when prompted.

5. **View Results**

   - The app will display:
     - The original word search grid.
     - A list of found words and their locations in the grid. Example:
       ```
       planet: ((14, 12), (9, 17))
       star: ((16, 0), (13, 3))
       ```
     - Performance metrics, such as time taken and memory used.

---

## **Example Output**

Below is an example of the solver’s output for a space-themed word search:

```
Solving word search from generated_word_searches\space\space_1.txt using words from words/space.txt...

Wordsearch grid:
h a n t e l e s c o p e b y n e h c v a
...

Found words and locations:
planet: ((14, 12), (9, 17))
star: ((16, 0), (13, 3))
galaxy: ((17, 5), (12, 10))
...

Time taken: 0.0361 seconds
Memory used: 0.01 MB
```

---

## **Tips for Best Results**

- Ensure the word search file is formatted correctly.
- Choose the theme and algorithm that best suit your puzzle’s size and complexity.
- Save or screenshot the results for future reference.

---

Enjoy solving or creating word searches with the Word Search Solver App!

