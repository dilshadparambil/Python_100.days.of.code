## Day 22: Pong Game  
A recreation of the classic Pong arcade game. This project involves building paddles, a ball, and implementing collision detection, scoring, and increasing difficulty as the game progresses.

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d22.py)  

### 🧠 Concepts Covered
- **Object-Oriented Programming (OOP)** with multiple classes (`Paddle`, `Ball`, `Scoreboard`)  
- **Event listeners** to handle paddle movements via keyboard input  
- **Collision detection** between ball, paddles, and walls  
- **Score keeping** with a dynamic scoreboard  
- **Game speed adjustments** as difficulty increases  
- **Encapsulation and modular design** for cleaner, reusable code  

### 📝 Instructions
1. **Set up the Main Screen**  
   - Create a screen using the `turtle` module.  
   - Set background color (black), dimensions (e.g., 800x600), and a suitable title.  
   - Configure tracer and update methods for smooth animations.  

2. **Create a Paddle that Responds to Key Presses**  
   - Build a `Paddle` class using `Turtle` as a base.  
   - Add methods `go_up()` and `go_down()` to move vertically.  
   - Bind keys (e.g., `Up`, `Down`) to control paddle movement.  

3. **Write the Paddle Class and Create the Second Paddle**  
   - Instantiate one paddle for the right side and another for the left side of the screen.  
   - Assign different key bindings (e.g., `w` and `s`) for the second paddle.  

4. **Write the Ball Class and Make the Ball Move**  
   - Create a `Ball` class to handle ball movement.  
   - Add methods for `move()`, `bounce_y()`, and `bounce_x()`.  
   - Ensure the ball moves continuously across the screen.  

5. **Add the Ball Bouncing Logic**  
   - If the ball collides with the top or bottom wall, reverse its y-direction.  
   - Keep the ball’s speed consistent while bouncing vertically.  

6. **Detect Collisions with the Paddle**  
   - If the ball is within a certain distance of a paddle and aligned with its y-coordinate, reverse the x-direction.  
   - Slightly increase ball speed after each paddle hit for difficulty progression.  

7. **Detect When the Ball Goes Out of Bounds**  
   - If the ball crosses the right boundary, reset its position and award a point to the left player.  
   - If the ball crosses the left boundary, reset and award a point to the right player.  

8. **Score Keeping and Changing the Ball Speed**  
   - Create a `Scoreboard` class to track and display scores on screen.  
   - Update the scoreboard dynamically after each point.  
   - Gradually increase ball speed as the game continues.  

💡 **Extra Challenge**:
- Add **sound effects** when the ball hits walls or paddles.  
- Display a **“Game Over” screen** when a player reaches a target winning score.  
- Introduce a **pause/restart feature** for better gameplay control.  
