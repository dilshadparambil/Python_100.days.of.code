## Day 23: Turtle Crossing Game  
A fun arcade-style game where the player controls a turtle trying to cross a busy road while avoiding moving cars. Each successful crossing increases the level and difficulty.

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d23.py)  

### 🧠 Concepts Covered
- Object-Oriented Programming with multiple classes  
- Event listeners and player controls  
- Collision detection between objects  
- Game loop and increasing difficulty  
- Scoreboard and level tracking  

### 📝 Instructions

#### 🎚️ Choose Your Difficulty
- **Normal 😎**: Use all Steps to complete the project.  
- **Hard 🤔**: Use only Steps 1 and 2 to complete the project.  
- **Expert 🤯**: Only use Step 1 to complete the project.  

1. **Check out how the gameplay works**  
   - Understand the mechanics: turtle moves up, cars move sideways, player avoids collisions.  

2. **Break down the Problem**  
   - Identify objects: Player (turtle), Cars, and Scoreboard.  
   - Define interactions between them.  

3. **Create the Player Behaviour**  
   - Implement movement for the turtle with keyboard controls.  
   - Reset position when it reaches the finish line.  

4. **Create the Car Behaviour**  
   - Generate multiple cars at random positions.  
   - Move cars across the screen at increasing speed.  

5. **Detect when the Turtle collides with a Car**  
   - If the player hits a car, end the game and display "Game Over".  

6. **Detect when the Player has reached the other side**  
   - When the turtle successfully crosses, reset its position and increase the game level.  

7. **Add the Scoreboard and Game Over sequence**  
   - Keep track of the level.  
   - Show "Game Over" when the player loses.  

💡 **Extra Challenge**:  
- Add multiple lanes with different speeds.  
- Randomize car colors for more variety.  
