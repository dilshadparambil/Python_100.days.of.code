## Day 18: Hirst Painting  
A program that generates a dot painting inspired by artist Damien Hirst using the turtle module.  

📄 [View Solution](solution.py) 📄 [View My Code](d18.py)  

### 🧠 Concepts Covered
- **Turtle graphics** for drawing shapes and dots  
- **Tuples** for storing and working with RGB color values  
- **Importing external modules** like `turtle`, `random`, and `colorgram`  
- **Loops** for repeating drawing actions  
- **Turtle positioning methods** like `.penup()`, `.setheading()`, `.forward()`, and `.goto()`  

### 📝 Instructions
1. **Extract Colors from an Image**  
   - Install and import the `colorgram` module.  
   - Use `colorgram.extract("image.jpg", number_of_colors)` to extract RGB colors from an image.  
   - Convert extracted colors into tuples `(r, g, b)` and store them in a list.  

2. **Set Up the Turtle Environment**  
   - Import the `turtle` module.  
   - Set color mode to RGB with `turtle.colormode(255)`.  
   - Create a turtle object, hide it, and set its speed to `"fastest"`.  

3. **Position the Turtle**  
   - Lift the pen with `.penup()`.  
   - Move the turtle to the bottom-left corner of the screen where the painting will start.  
   - Use `.setheading(angle)` and `.forward(distance)` to adjust positioning.  

4. **Draw the Dot Painting**  
   - Use a **nested loop** to create rows and columns of dots.  
   - Inside the inner loop:  
     - Pick a random color from the extracted color list using `random.choice()`.  
     - Draw a dot with `turtle.dot(size, color)`.  
     - Move forward a set distance to space the dots evenly.  
   - At the end of each row, move the turtle up and reset position to the start of the next row.  

5. **Complete the Artwork**  
   - Repeat until the desired grid (e.g., 10x10) is filled.  
   - Use `turtle.done()` to keep the painting window open once complete.  

💡 **Extra Challenge**:  
- Allow the user to customize the grid size (e.g., 20x20).  
- Randomize dot sizes for variation.  
- Use multiple images to generate different color palettes.  
