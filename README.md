# 🐍 100 Python Projects: 100 Days of Code

Welcome to my journey of completing 100 Python projects in 100 days. This challenge is aimed at improving my Python skills by building real-world mini-projects every day.

---

## 📅 Table of Contents

| Day | Project Title           | Link                                   |
|-----|-------------------------|----------------------------------------|
| 1   | Band Name Generator     | [Day 1](#day-1-Band-Name-Generator)    |
| 2   | Tip Calculator          | [Day 2](#day-2-Tip-Calculator)         |
| 3   | Treasure Island         | [Day 3](#day-3-Treasure-Island)        |
| 4   | Rock Paper Scissors     | [Day 4](#day-4-Rock-Paper-Scissors)    |
| 5   | Password Generator      | [Day 5](#day-5-Password-Generator)     |
| 6   | Reeborg's World: Maze   | [Day 6](#day-6-Reeborgs-World-Maze)    |
| 7   | Hangman                 | [Day 7](#day-7-Hangman)                |
| 8   | Caesar Cipher           | [Day 8](#day-8-Caesar-Cipher)          |



---

## 📘 Projects

### Day 1: Band Name Generator

A simple project that generates a band name using the city you grew up in and your pet’s name.

📄 [View the code](Project_files/d1.py) [🔼 Back to Top](#-table-of-contents)

#### 🧠 Concepts Covered
- Printing to the console
- Receiving user input
- String concatenation
- Basic Python syntax

#### 📝 Instructions
1. Create a greeting for your program.
2. Ask the user for the city that they grew up in and store it in a variable.
3. Ask the user for the name of a pet and store it in a variable.
4. Combine the name of their city and pet and show them their band name.
5. Make sure the input cursor shows on a new line.

---

### Day 2: Tip Calculator

A simple calculator that helps you split a bill, including tip, among multiple people.

📄 [View the code](Project_files/d2.py) [🔼 Back to Top](#-table-of-contents)

#### 🧠 Concepts Covered
- Data types
- Arithmetic operations
- Type checking
- Type conversions (str(), int(), float())
- Flooring & rounding
- Formatted strings (f-strings)

#### 📝 Instructions
1. Ask the user for the total bill amount.
2. Ask for the tip percentage they want to give.
3. Ask how many people to split the bill between.
4. Calculate how much each person should pay.
5. Format the result to 2 decimal places for currency.

#### 💡 Example
```text
If the bill was $150.00, split between 5 people, with 12% tip:
(150.00 / 5) * 1.12 = 33.6

After formatting:
Each person pays: 33.60
```

---

### Day 3: Treasure Island

Your goal today is to build a "Choose Your Own Adventure" game.  
Using conditional logic and flow control, this text-based game leads the player on a short adventure to find a hidden treasure.

📄 [View the code](Project_files/d3.py) [🔼 Back to Top](#-table-of-contents)

#### 🧠 Concepts Covered
- Conditional statements (`if`, `elif`, `else`)  
- Logical operators (`and`, `or`)  
- Code blocks and indentation  
- Scope and nesting logic

#### 📝 Instructions
1. Greet the player and set the adventure theme.
2. Present choices using `input()` and handle the response with `if` conditions.
3. Guide the user through different paths based on their inputs:
   - Left or Right
   - Swim or Wait
   - Red, Blue, or Yellow door
4. Use nested conditionals to follow the flowchart logic.
5. Print game-over or victory messages accordingly.

Use this [flowchart](assets/d3flow.png) to design your adventure game logic

---

### Day 4: Rock Paper Scissors  

You are going to build a Rock, Paper, Scissors game.  
You will use randomisation and lists to simulate the classic hand game between the user and the computer.

📄 [View the code](Project_files/d4.py) [🔼 Back to Top](#-table-of-contents)

#### 🧠 Concepts Covered
- Python modules  
- `random` module (`randint`)  
- Lists and indexing  
- Conditional logic and comparison  
- User input validation

#### 📝 Instructions
1. Create a list of game choices: Rock, Paper, and Scissors.  
2. Ask the user to input their choice (0 for Rock, 1 for Paper, 2 for Scissors).  
3. Use the `random` module to let the computer randomly select a choice.  
4. Compare both choices using conditions to determine the winner.  
5. Display the choices and result (Win, Lose, or Draw).  
6. Handle invalid inputs gracefully.

---

### Day 5: Password Generator  
This program generates a secure password based on user preferences for letters, symbols, and numbers.  
You'll practice combining loops and lists to build both simple and randomized password generators.

📄 [View the code](Project_files/d5.py) [🔼 Back to Top](#-table-of-contents)

#### 🧠 Concepts Covered
- `for` loops and `range()`  
- Code blocks and indentation  
- List creation and manipulation  
- Randomisation (`random` module)  
- User input handling  
- String joining and shuffling

#### 📝 Instructions
1. Ask the user:
   - How many **letters** they want in the password  
   - How many **symbols**  
   - How many **numbers**  
2. Generate the required number of characters using:
   - A list of letters (uppercase and lowercase)  
   - A list of symbols (`!`, `#`, `$`, etc.)  
   - A list of digits (`0-9`)  
3. Combine the selected characters into a password.

#### 🟢 Easy Version  
Generate the password in a fixed order:  
**`Letters → Symbols → Numbers`**

💡Example:  
```text
Input: 4 letters, 2 symbols, 3 numbers  
Output: fgdx$*924
```

Characters are grouped together by type.

#### 🔴 Hard Version  
Generate the password with **`randomized order`**:  
Characters are shuffled so there's **no pattern**.

💡Example:  
```text
Input: 4 letters, 2 symbols, 3 numbers  
Output: x$d24g*f9
```
You will need to:
- Combine all selected characters into one list  
- Use `random.shuffle()` to mix them  

---

### Day 6: Reeborg's World: Maze  
Reeborg is lost in a maze!  
Your task is to write a program that helps Reeborg find the exit by following the **right-hand rule** (always follow the wall on your right).  
🌐 [Try it on Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)  

📄 [View the code](Project_files/d6.py) [🔼 Back to Top](#-table-of-contents)  

#### 🧠 Concepts Covered
- `while` loops and conditionals  
- `if / elif / else` branching  
- Custom functions  
- Code blocks and indentation  
- Boolean conditions and negation (`not`)  
- Environment-based logic using:
  - `move()`  
  - `turn_left()`  
  - `front_is_clear()` / `wall_in_front()`  
  - `right_is_clear()` / `wall_on_right()`  
  - `at_goal()`

#### 📝 Instructions
1. Reeborg must **keep moving** until it reaches the goal (`at_goal()`).
2. Reeborg should:
   - Turn **right** if there’s a clear path.
   - Else, move **straight ahead** if the path is clear.
   - Else, turn **left** as a last resort.
3. You'll need to define a custom `turn_right()` function (Reeborg only supports `turn_left()`).
4. Use a `while` loop to repeatedly evaluate Reeborg’s surroundings and make decisions.

💡 **Bonus Tips**:  
  
- This is a classic right-wall-following algorithm.
- The logic mimics placing your hand on the right wall and walking through the maze.

---

### Day 7: Hangman  
A classic word-guessing game where the user has to guess the letters of a hidden word before running out of lives.  
You'll build this project step by step, using loops, conditionals, and functions while improving modular thinking.

📄 [View the code](Project_files/d7.py) [🔼 Back to Top](#-table-of-contents)

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

Use this [flowchart](assets/d7flow.png) to design your Hangman

💡 **Bonus Tips**:  
  
- Break your code into functions as it grows.  
- You can enhance the game with difficulty settings or replayability.

---

### Day 8: Caesar Cipher  
Build your own text encryption and decryption tool using Caesar Cipher logic!  
This project introduces function inputs, parameter handling, and simple text transformations.

📄 [View the code](Project_files/d8.py) [🔼 Back to Top](#-table-of-contents)

#### 🧠 Concepts Covered
- Functions with inputs  
- Parameters and arguments  
- Positional vs keyword arguments  
- Indexing in lists  
- String and character manipulation  
- Looping through strings  
- Preserving non-alphabet characters  
- Creating reusable logic with control flow

#### 📝 Instructions

1. Create a function called `encrypt()` that takes `original_text` and `shift_amount` as parameters.
   - Shift each letter in the text **forwards** by the `shift_amount`.
   - Use `alphabet.index()` to find positions.
   - Handle wrap-around from `'z'` to `'a'`.
   - Example:  
     ```python
     plain_text = "hello"
     shift_amount = 1
     # Output: ifmmp
     ```

2. Create a function called `decrypt()` that:
   - Shifts each letter **backwards** by the `shift_amount`.
   - Reverses the encryption process.

3. Combine both `encrypt()` and `decrypt()` into a single function called `caesar()`.
   - Add a `direction` input to determine which action to take.
   - Call this function using user inputs for `direction`, `text`, and `shift`.

4. Handle edge cases:
   - If the user enters numbers, symbols, or spaces, preserve them in the result.
     - Example:  
       ```text
       original_text = "meet me at 3!"
       cipher_text = "xxxx xx xx 3!"  # letters shifted, digits/symbols untouched
       ```

5. Add a restart option:
   - Ask the user if they want to encode/decode another message:
     ```text
     Type 'yes' if you want to go again. Otherwise, type 'no'.
     ```

💡 **Bonus Tips**:  

- Use `modulus (%)` to wrap around the alphabet if shifting past `'z'`.  
- Convert text to lowercase before processing for consistency.  
- Use a `while` loop to allow restarting the cipher repeatedly.

---

### Day 9:

