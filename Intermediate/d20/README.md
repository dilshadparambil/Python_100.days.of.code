## Day 20: Snake Game Part 1  
The first part of building the classic Snake Game using Python’s `turtle` module. This stage focuses on creating the snake body, moving it across the screen, and controlling its direction with keyboard inputs.

📄 [View Solution](solution/solution.py) 📄 [View My code](my_code/d20.py)   

### 🧠 Concepts Covered
- Turtle graphics for game development  
- Creating multiple objects (snake segments)  
- Loops for movement updates  
- Functions and methods for controlling behavior  
- Event listeners for keyboard controls  

### 📝 Instructions
1. **Create Snake Body**  
   - Initialize the snake with 3 square-shaped turtle objects positioned in a line.  
   - Store them in a list to manage as the snake’s body.  

2. **Move Snake**  
   - Write a `move()` function to shift each segment to the position of the previous one.  
   - Move the head forward continuously to create the snake’s motion.  

3. **Control Snake**  
   - Use event listeners to detect key presses (`Up`, `Down`, `Left`, `Right`).  
   - Change the snake’s heading while preventing 180° turns (cannot go directly backward).  

💡 **Extra Challenge**:
- Add boundaries to the screen so the snake cannot go out.  
- Increase snake length whenever an event occurs (to prepare for food in Part 2).  


