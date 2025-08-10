### Day 7: Hangman  
A classic word-guessing game where the user has to guess the letters of a hidden word before running out of lives.  
You'll build this project step by step, using loops, conditionals, and functions while improving modular thinking.

📄 [View the code](Project_files/d07/solution.py) [🔼 Back to Top](#-table-of-contents)

#### 🧠 Concepts Covered
- `while` and `for` loops  
- Conditional logic  
- String manipulation  
- Lists and indices  
- Importing from other Python files  
- ASCII art  
- User input and validation  
- Game state tracking (win/lose conditions)

#### 📝 Instructions

You will implement a full-featured Hangman game by following a sequence of development steps:

1. Randomly choose a word from a predefined `word_list` and store it in `chosen_word`. Print it for testing.
2. Ask the user to guess a letter and convert the input to lowercase. Store it in the variable `guess`.
3. Loop through each letter in `chosen_word` and:
   - Print `"Right"` if the guess is correct
   - Print `"Wrong"` otherwise
4. Create a `display` list with one `_` for each letter in `chosen_word`.<br />This will represent the user's progress visually.
5. Loop through `chosen_word`. If `guess` matches a letter, update the `display` list at that position.
6. Use a `while` loop to allow the user to guess repeatedly until there are no `_` characters left in `display`.
7. Ensure that previous correct guesses are preserved in the `display`.
8. Create a variable `lives` and set it to 6.
9. If the guessed letter is **not** in `chosen_word`, subtract 1 from `lives`.<br />If `lives` reaches 0, the game ends with "You lose."
10. Print the corresponding ASCII hangman image from the `stages` list based on the current number of lives.
11. Move your word list into a separate file `d7_words.py` and import it.
12. Move the `stages` list into `d7_art.py` and import it.
13. Add a game logo stored in `d7_art.py` and print it at the start of the game.
14. If the user guesses a letter they've already tried, show a warning and **do not** subtract a life.
15. If the letter is not in the word, inform the user:<br />`You guessed d, that's not in the word. You lose a life.`
16. Add a message to show how many lives are remaining:<br />`**************************** <???>/6 LIVES LEFT ****************************`
17. If the user loses, reveal the correct word:<br />`IT WAS <Correct Word>! YOU LOSE`

Use this [flowchart](Project_files/d07/d7flow.png) to design your Hangman

💡 **Bonus Tips**:  
  
- Break your code into functions as it grows.  
- You can enhance the game with difficulty settings or replayability.

---