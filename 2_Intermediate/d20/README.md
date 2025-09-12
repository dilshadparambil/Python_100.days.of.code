## Day 20: Snake Game (Part 1)  
The first stage of building the classic Snake game using the turtle graphics module.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d20.py)  

### 🧠 Concepts Covered
- **Object-Oriented Programming (OOP)** with classes  
- **Creating and controlling multiple objects** (snake segments)  
- **Using loops** for continuous movement  
- **Key event listeners** for user input and interaction  
- **Game design basics** (separating logic into different methods)  

### 📝 Instructions
1. **Set Up the Screen**  
   - Import `turtle` and configure the screen with `Screen()`.  
   - Set background color (e.g., `"black"`), title (e.g., `"Snake Game"`), and size (e.g., `600x600`).  
   - Use `screen.tracer(0)` to control screen updates manually for smoother animation.  

2. **Create the Snake Body**  
   - Initialize a list to hold snake segments.  
   - Use a loop to generate 3 square turtle objects.  
   - Position them side by side (e.g., at `(0,0)`, `(-20,0)`, `(-40,0)`) to form the starting snake.  
   - Append each turtle segment to the list.  

3. **Move the Snake**  
   - Define a `move()` method in a `Snake` class.  
   - Loop through the segments in reverse order:  
     - Each segment moves to the position of the segment in front of it.  
   - Move the head forward a fixed distance (e.g., `20` pixels).  
   - Update the screen with `screen.update()` inside the game loop.  

4. **Control the Snake**  
   - Bind arrow keys (`Up`, `Down`, `Left`, `Right`) using `screen.listen()` and `onkey()`.  
   - Write methods like `up()`, `down()`, `left()`, and `right()` to change the snake’s heading.  
   - Add logic to prevent the snake from reversing onto itself (e.g., cannot go from left to right immediately).  

5. **Run the Game Loop**  
   - Create a `while` loop that:  
     - Calls `move()` repeatedly.  
     - Uses `time.sleep(0.1)` for consistent speed.  
     - Keeps the game running until manually stopped.  

💡 **Extra Challenge**:  
- Add a function to extend the snake when it "eats".  
- Make the game restart automatically after closing.  
- Add boundary detection to stop the snake at screen edges.  
