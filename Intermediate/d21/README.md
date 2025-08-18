## Day 21: Snake Game Part 2  
The second part of the Snake Game project. This stage enhances the game by adding food, score tracking, and collision detection with walls and the snake’s own tail.

📄 [View Solution](solution/solution.py) 📄 [View My code](my_code/d21.py)   

### 🧠 Concepts Covered
- Inheritance in classes  
- List slicing for handling snake segments  
- Collision detection with objects and boundaries  
- Updating the scoreboard dynamically  
- Game over conditions  

### 📝 Instructions
4. **Detect Collision with Food**  
   - Place a `Food` object randomly on the screen.  
   - If the snake’s head collides with the food:  
     - Extend the snake by adding a new segment.  
     - Refresh the food to a new random position.  
     - Increase the score.  

5. **Create a Scoreboard**  
   - Build a `Scoreboard` class to track and display the score.  
   - Update the score whenever the snake eats food.  
   - Show “GAME OVER” when the player loses.  

6. **Detect Collision with Wall**  
   - Check if the snake’s head crosses the screen boundaries.  
   - If true, end the game and display “GAME OVER”.  

7. **Detect Collision with Tail**  
   - Loop through all segments of the snake except the head.  
   - If the head collides with any body part, the game ends.  

💡 **Extra Challenge**:
- Add a high-score feature that persists between games.  
- Make the snake move faster as the score increases.  
