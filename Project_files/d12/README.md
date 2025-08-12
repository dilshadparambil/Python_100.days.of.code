### Day 12: Number Guessing Game  
A simple number guessing game where the player tries to guess a randomly chosen number between 1 and 100.  
The game adjusts difficulty levels and tracks the number of remaining attempts.

📄 [View the code](solution.py)  

#### 🧠 Concepts Covered
- Functions with inputs and outputs  
- Conditional logic (`if / elif / else`)  
- Random number generation (`random.randint()`)  
- Variables and scope  
- Loops for repeated guessing  
- Difficulty settings

#### 📝 Instructions
1. **Function to check the guess**:
   - Compare the user’s guess to the actual answer.  
   - Print feedback: `"Too high"`, `"Too low"`, or `"Correct"`.  
   - Reduce the number of turns if incorrect.

2. **Function to set difficulty**:
   - Ask the player to choose a difficulty level:
     - `"easy"` → 10 attempts  
     - `"hard"` → 5 attempts

3. **Generate a random number**:
   ```python
   import random
   answer = random.randint(1, 100)
   ```

4. **Game loop**:
   - Ask the user for a guess.  
   - Check the guess using the check function.  
   - If incorrect and turns remain → Let them guess again.  
   - If correct → End the game with a win message.  
   - If out of turns → Reveal the answer and end the game.

💡 **Extra Challenge**:
- Allow the player to restart the game after winning or losing.  
- Provide hints when guesses are close to the actual answer.

---
