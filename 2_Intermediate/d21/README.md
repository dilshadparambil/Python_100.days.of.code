## Day 21: Snake Game (Part 2)  
Enhancements to the Snake game with food, scoring, and collisions.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d21.py)   

### 🧠 Concepts Covered
- **Inheritance between classes** (extending functionality)  
- **Slicing lists** for handling segments of the snake  
- **Collision detection** with objects, walls, and self  
- **Updating scores dynamically** using a separate scoreboard class  
- **Game over logic** and modular code structure  

### 📝 Instructions
4. **Detect Collision with Food**  
   - Create a `Food` class that inherits from `Turtle`.  
   - Configure it as a small circle with a random color.  
   - Place it at random positions on the screen using `random.randint()`.  
   - If the snake’s head is within a certain distance of the food (e.g., `<15` pixels):  
     - Relocate the food.  
     - Extend the snake by adding a new segment to the tail.  
     - Increase the score.  

5. **Create a Scoreboard**  
   - Build a `Scoreboard` class that also inherits from `Turtle`.  
   - Display the current score at the top of the screen.  
   - Add a method to update the score whenever food is eaten.  
   - Add a `game_over()` method to display “GAME OVER” in the center when the game ends.  

6. **Detect Collision with Wall**  
   - Check the x and y coordinates of the snake’s head.  
   - If the head’s position is outside the boundaries (e.g., ±280 for a 600x600 screen):  
     - Stop the game loop.  
     - Call the `game_over()` method in the `Scoreboard`.  

7. **Detect Collision with Tail**  
   - Loop through all snake segments except the head (using list slicing).  
   - If the head’s distance from any segment is <10 pixels:  
     - Stop the game.  
     - Call the `game_over()` method.  

💡 **Extra Challenge**:  
- Add levels where speed increases as the score gets higher.  
- Save the high score in a file so it persists between game sessions.  
- Add a restart option after game over.  
