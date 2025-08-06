# 🐍 100 Python Projects: 100 Days of Code

Welcome to my journey of completing 100 Python projects in 100 days. This challenge is aimed at improving my Python skills by building real-world mini-projects every day.

---

## 📅 Table of Contents

| Day | Project Title           | Link                                   |
|-----|-------------------------|----------------------------------------|
| 1   | Band Name Generator     | [Day 1](#day-1-band-name-generator)    |
| 2   | Tip Calculator          | [Day 2](#day-2-tip-calculator)         |
| 3   | Treasure Island         | [Day 3](#day-3-treasure-island)        |
| 4   | Rock Paper Scissors     | [Day 4](#day-4-rock-paper-scissors)    |
| 5   | Password Generator      | [Day 5](#day-5-password-generator)     |


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

### Day 6:
