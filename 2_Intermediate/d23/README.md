## Day 23: Turtle Crossing Game  
A fun arcade-style game where the player controls a turtle trying to cross a busy road while avoiding moving cars. Each successful crossing increases the level and difficulty.

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d23.py)  

### 🧠 Concepts Covered
- Object-Oriented Programming (OOP) with multiple classes (`Player`, `CarManager`, `Scoreboard`)  
- Event listeners and player controls using `onkey()`  
- Collision detection between moving objects  
- Infinite game loop with dynamic difficulty scaling  
- Scoreboard for tracking levels and displaying Game Over  

### 📝 Instructions  

#### 🎚️ Choose Your Difficulty
- **Normal 😎**: Use all steps to complete the project.  
- **Hard 🤔**: Use only Steps 1 and 2 to complete the project.  
- **Expert 🤯**: Only use Step 1 to complete the project.  

1. **Check out how the gameplay works**  
   - The player controls a turtle that moves upward with key presses.  
   - Cars move horizontally across the screen.  
   - The goal is to reach the finish line without colliding with cars.  

2. **Break down the Problem**  
   - Identify game components:  
     - **Player** → the turtle character.  
     - **Cars** → obstacles moving across the screen.  
     - **Scoreboard** → displays the current level and Game Over message.  
   - Define interactions: player movement, car generation and movement, collision detection, and scoring.  

3. **Create the Player Behaviour**  
   - Implement the `Player` class using `Turtle`.  
   - Add a method to move the turtle upward on key press (`Up` arrow).  
   - Reset the turtle’s position when it reaches the top.  

4. **Create the Car Behaviour**  
   - Implement the `CarManager` class.  
   - Randomly generate cars with different colors.  
   - Move cars across the screen continuously.  
   - Increase car speed as levels progress to raise difficulty.  

5. **Detect when the Turtle collides with a Car**  
   - Use distance checks between the player and cars.  
   - If a collision occurs, stop the game loop and display "Game Over".  

6. **Detect when the Player has reached the other side**  
   - If the turtle reaches the finish line:  
     - Reset its position to the start.  
     - Increase the level on the scoreboard.  
     - Increase the speed of the cars.  

7. **Add the Scoreboard and Game Over sequence**  
   - Implement a `Scoreboard` class.  
   - Track the player’s current level.  
   - Display updated level each time the player successfully crosses.  
   - Show "Game Over" when the player collides with a car.  

💡 **Extra Challenge**:  
- Add multiple lanes with different car speeds.  
- Randomize car colors for variety.  
- Add sound effects for collisions and level-ups.  
