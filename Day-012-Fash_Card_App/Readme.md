# Flashy - French Flashcard App 🇫🇷

Flashy is a simple desktop flashcard application built with Python's Tkinter and Pandas. It helps users learn French vocabulary by displaying a word, automatically showing the translation after a brief period, and allowing the user to mark words as known or unknown to refine their study list.

## ✨ Features

- **Initial Load:** Loads words from `./data/words_to_learn.csv` if it exists (for continued study), otherwise loads the full set from `./data/french_words.csv`.
- **Timed Flip:** Automatically displays the English translation 3 seconds after the French word appears.
- **Save Progress:**
    - If a word is marked **Known (✅)**, it is removed from the current session's study list.
    - If the user quits the application (or hits 'Not Known' and the file is updated), the words remaining in the session's list are saved to `./data/words_to_learn.csv` for the next session.
- **Simple UI:** A clean, engaging user interface with card images.

## 🚀 Getting Started

### Prerequisites

You will need Python installed on your system. This project also requires the `tkinter` (usually included with Python) and `pandas` libraries.

```bash
pip install pandas
````

### Installation and Setup

1.  **Clone the repository** (assuming this is part of a larger project) or save the files in a dedicated folder.
2.  **Setup Data:**
      * Ensure you have a CSV file named `french_words.csv` inside a `./data` folder, with columns named **"French"** and **"English"**.
      * Create a `./data` folder in the root of your project: `mkdir data`
      * Example content for `french_words.csv`:
        ```csv
        French,English
        bonjour,hello
        au revoir,goodbye
        pomme,apple
        ...
        ```
3.  **Setup Images:**
      * Create an `./images` folder.
      * Place the required image files inside it:
          * `card_front.png`
          * `card_back.png`
          * `right.png` (for the "Known" button)
          * `wrong.png` (for the "Not Known" button)

### Running the Application

Execute the main Python file (`main.py` in the original structure, or the file containing the `Tk` and `mainloop` calls):

```bash
python main.py
```

## 📋 Code Structure

The application is logically split into two main components:

### `main.py` (or your main application file)

  - Sets up the main Tkinter window, title, and background color.
  - Instantiates the `GenerateInterface` class.

### `generate_card.py` (or the file containing the class)

  - **Data Loading:** Uses `pandas` to load the word list, prioritizing `words_to_learn.csv`.
  - **`GenerateInterface` Class (inherits from `Canvas`):**
      - Initializes the canvas and loads card images.
      - **`change_french()`:** Selects a random word, displays the French side, and sets a 3-second timer for the flip.
      - **`change_english()`:** Flips the card, displays the English translation, and adds the "Known" and "Not Known" buttons.
      - **`word_known()`:** Removes the current word from the study list and calls `change_french()` for the next word.
      - **`word_not_known()`:** Saves the **remaining** words in the study list to `words_to_learn.csv` (this part of the logic seems to save the *current* word list, and may need refinement to only save on exit or after multiple 'Not Known' actions, but this is how the provided code works).

## 🛠️ Dependencies

  - `tkinter` (standard Python library)
  - `pandas`
  - `random`

## 💡 Potential Enhancements

  - **Error Handling:** Add more robust error handling for missing image or data files.
  - **Permanent Removal:** Update `word_known()` to write the reduced list to `words_to_learn.csv` after a word is successfully learned to make the progress permanent across sessions.
  - **Card Flipping Logic:** Currently, `create_image` and `create_text` are called every time, which redraws the entire card. A more efficient approach would be to use `itemconfigure` or `delete` existing text/images before redrawing.

<!-- end list -->

```
```
