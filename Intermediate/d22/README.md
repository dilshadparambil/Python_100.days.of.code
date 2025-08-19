## Day 22: Pong Game  
A recreation of the classic Pong arcade game. This project involves building paddles, a ball, and implementing collision detection, scoring, and increasing difficulty as the game progresses.

📄 [View Solution](solution/solution.py) 📄 [View My code](my_code/d22.py)  

### 🧠 Concepts Covered
- Object-Oriented Programming with multiple classes  
- Event listeners for paddle movement  
- Collision detection with walls and paddles  
- Score keeping and updating dynamically  
- Adjusting object speed for difficulty progression  

### 📝 Instructions
1. **Set up the Main Screen**  
   - Create the game screen with `turtle` graphics.  
   - Define background color, dimensions, and title.  

2. **Create a Paddle that Responds to Key Presses**  
   - Build a paddle that can move up and down using keyboard events.  

3. **Write the Paddle Class and Create the Second Paddle**  
   - Encapsulate paddle behavior into a class.  
   - Instantiate two paddles for each side of the screen.  

4. **Write the Ball Class and Make the Ball Move**  
   - Create a `Ball` class that handles ball movement.  
   - Continuously update its position.  

5. **Add the Ball Bouncing Logic**  
   - Detect collisions with the top and bottom walls.  
   - Reverse ball direction when it hits the wall.  

6. **How to Detect Collisions with the Paddle**  
   - If the ball is near a paddle and within its y-range, bounce it back.  

7. **How to Detect when the Ball goes Out of Bounds**  
   - If the ball crosses left/right boundaries, reset position.  
   - Award a point to the opposing player.  

8. **Score Keeping and Changing the Ball Speed**  
   - Maintain player scores on screen.  
   - Increase ball speed after every successful paddle hit for added challenge.  

💡 **Extra Challenge**:
- Add sound effects when the ball bounces.  
- Display a “Game Over” screen when a player reaches a winning score.  
 

