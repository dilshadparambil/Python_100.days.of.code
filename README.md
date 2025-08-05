# 🐍 100 Python Projects: 100 Days of Code

Welcome to my journey of completing 100 Python projects in 100 days. This challenge is aimed at improving my Python skills by building real-world mini-projects every day.

---

## 📅 Table of Contents

| Day | Project Title           | Link                                |
|-----|----------------------   |-------------------------------------|
| 1   | Band Name Generator     | [Day 1](#day-1-band-name-generator) |
| 2   | Tip Calculator          | [Day 2](#day-2-tip-calculator)      |
| 3   | Treasure Island         | [Day 3](#day-3-treasure-island)     |
| 4   | Rock Paper Scissors     | [Day 4](#day-4-rock-paper-scissors)     |


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
