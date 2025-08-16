## Day 18: Hirst Painting  
A Python program that recreates a dot-style artwork inspired by Damien Hirst’s spot paintings.  
Using the `turtle` graphics library, the program generates a grid of colored dots sampled from an image.

📄 [View Solution](solution.py) 📄 [View My Code](d18.py)  

### 🧠 Concepts Covered
- Turtle graphics for drawing  
- Working with tuples (RGB color values)  
- Importing modules (`turtle`, `colorgram`)  
- Using loops for grid creation  
- Random color selection from extracted palettes  

### 📝 Instructions
1. Import necessary modules (`turtle`, `colorgram`, `random`).  
2. Extract a color palette from an image (`image.jpg`) using the `colorgram` module.  
3. Store the extracted colors as a list of tuples (R, G, B).  
4. Configure the turtle: hide it, set speed, and move to a starting position.  
5. Create a grid of dots using `turtle.dot(size, color)`.  
   - Use nested loops to move across rows and columns.  
   - Select random colors from the palette for each dot.  
6. Generate a final artwork similar to Damien Hirst’s style.

💡 **Extra Challenge**:
- Allow the user to define grid size and dot spacing.  
- Extract different palettes from various images.  
- Save the generated artwork as an image file.  
