```markdown
### Day 11: Blackjack  
A text-based Blackjack game where you play against the computer dealer.  
Follow the house rules, apply game logic, and make strategic decisions to win.

📄 [View the code](solution.py)  
🔗 [🃏 Try Blackjack Online](https://games.washingtonpost.com/games/blackjack/)

#### 🧠 Concepts Covered
- Functions with inputs and outputs  
- Lists and list methods (`append()`, `remove()`)  
- Conditional statements  
- Loops and game state control  
- Importing and using ASCII art (`art.py`)  
- Comparing game results with a `compare()` function

#### 📝 House Rules
- The deck is unlimited in size.  
- No jokers are included.  
- Jack/Queen/King count as **10**.  
- Ace counts as **11** or **1**.  
- Deck of cards:
  ```python
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  ```
- Cards are not removed after being drawn.  
- Computer acts as the dealer.  

#### 📝 Instructions
1. **Create a `deal_card()` function** to return a random card from the `cards` list.  
2. Deal **2 cards** each to `user_cards` and `computer_cards`.  
3. **Create `calculate_score()`**:
   - Returns the sum of card values.  
   - Blackjack (Ace + 10 in 2 cards) returns `0` as a special case.  
   - Adjust Ace from `11` to `1` if total score exceeds 21.  
4. **Game Flow**:
   - Check for blackjack or score over 21 → game ends.  
   - If not over, ask if the user wants another card:
     - If **yes** → Add card to `user_cards` and recheck score.  
     - If **no** → Move to computer’s turn.  
   - Computer draws cards until score ≥ 17.  
5. **Create `compare(user_score, computer_score)`**:
   - If scores equal → Draw.  
   - If computer has blackjack → Player loses.  
   - If player has blackjack → Player wins.  
   - If player > 21 → Player loses.  
   - If computer > 21 → Player wins.  
   - Otherwise, highest score wins.  
6. **Restart Option**:
   - Ask if the user wants to play again.  
   - If yes → Clear console and restart game with logo from `art.py`.

💡 **Hints**:
- [Requirement Breakdown](d11req.png)  
- [Flowchart Download]()  
- Use `random.choice()` for card selection.  
- Keep checking scores after each draw until the game ends.

---
```
