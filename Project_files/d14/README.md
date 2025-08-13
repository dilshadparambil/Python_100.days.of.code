## Day 14: Higher Lower Game  
A comparison game where the player guesses which Instagram account has more followers.  
Based on the classic [Higher Lower Game](https://www.higherlowergame.com/), but using a custom dataset.

📄 [View Solution](solution.py) 📄 [View My code](d14.py)  

### 🧠 Concepts Covered
- Random selection from a list of dictionaries  
- Functions with inputs and outputs  
- Loops for repeatable gameplay  
- Conditional logic for comparing data  
- Score tracking  
- Clearing the console output

### 📝 Instructions
1. **Display ASCII art** from `art.py` at the start of the game.  
2. **Randomly generate two accounts** from the game data file (`game_data.py`).  
3. **Show formatted account details** (name, description, country) to the player without revealing follower counts.  
4. Ask the user to **guess which account has more followers** (`A` or `B`).  
5. **Clear the screen** after the guess.  
6. **Check the guess**:
   - Retrieve follower counts for both accounts.  
   - Determine if the guess was correct.  
   - If correct → Increment score and make **account B** become **account A** for the next round.  
   - If wrong → End the game and show final score.  
7. Repeat steps 2–6 until the player guesses incorrectly.

💡 **Extra Challenge**:
- Add more data entries to `game_data.py` for variety.  
- Implement a "best score" tracker.  
- Add a delay between rounds for better pacing.

---
