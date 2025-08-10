### Day 6: Reeborg's World: Maze  
Reeborg is lost in a maze!  
Your task is to write a program that helps Reeborg find the exit by following the **right-hand rule** (always follow the wall on your right).  
🌐 [Try it on Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)  

📄 [View the code](Project_files/d06/solution.py) [🔼 Back to Top](#-table-of-contents)  

#### 🧠 Concepts Covered
- `while` loops and conditionals  
- `if / elif / else` branching  
- Custom functions  
- Code blocks and indentation  
- Boolean conditions and negation (`not`)  
- Environment-based logic using:
  - `move()`  
  - `turn_left()`  
  - `front_is_clear()` / `wall_in_front()`  
  - `right_is_clear()` / `wall_on_right()`  
  - `at_goal()`

#### 📝 Instructions
1. Reeborg must **keep moving** until it reaches the goal (`at_goal()`).
2. Reeborg should:
   - Turn **right** if there’s a clear path.
   - Else, move **straight ahead** if the path is clear.
   - Else, turn **left** as a last resort.
3. You'll need to define a custom `turn_right()` function (Reeborg only supports `turn_left()`).
4. Use a `while` loop to repeatedly evaluate Reeborg’s surroundings and make decisions.

💡 **Bonus Tips**:  
  
- This is a classic right-wall-following algorithm.
- The logic mimics placing your hand on the right wall and walking through the maze.

---