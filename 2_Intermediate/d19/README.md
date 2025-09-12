## Day 19: Turtle Racing  
A turtle racing game where multiple turtles compete across the screen and the user bets on which turtle will win.  

📄 [View Solution](solution.py) 📄 [View My Code](d19.py)  

### 🧠 Concepts Covered
- **Turtle graphics** for drawing and movement  
- **Event listeners** (`screen.listen()`, `onkey()`) for interactivity  
- **Higher-order functions** (passing functions as arguments to listeners)  
- **Multiple instances of a class** (creating several turtle racers)  
- **Loops** for continuous updates  
- **Random movement** to simulate racing  

### 📝 Instructions
1. **Set Up the Screen**  
   - Import `turtle` and create a screen object.  
   - Set screen dimensions (e.g., `screen.setup(width=500, height=400)`).  
   - Use `screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color:")` to let the user place a bet.  

2. **Create Turtle Racers**  
   - Define a list of turtle colors (e.g., `["red", "orange", "yellow", "green", "blue", "purple"]`).  
   - Loop through the list to create one turtle per color.  
   - Position each turtle at the left side of the screen with unique `y`-coordinates so they appear in a row.  
   - Set each turtle’s shape to `"turtle"` and lift the pen with `.penup()`.  

3. **Draw the Starting and Finish Lines** *(optional for visuals)*  
   - Use a turtle object to draw a vertical line at the start and another at the finish.  
   - This helps visually separate the track.  

4. **Start the Race**  
   - Use a `while` loop to repeatedly move each turtle forward by a random distance (e.g., `randint(0, 10)`).  
   - Keep looping until at least one turtle crosses the finish line (`xcor()` > finish line position).  

5. **Check for Winner**  
   - When a turtle reaches the finish line, record its color as the winner.  
   - Compare the winning color with the user’s bet.  
   - Print the result:  
     - `"You’ve won! The <color> turtle is the winner!"`  
     - `"You’ve lost! The <color> turtle won the race."`  

6. **Keep Window Open**  
   - Call `screen.exitonclick()` so the program closes only when the user clicks on the window.  

💡 **Extra Challenge**:  
- Add a countdown before the race starts.  
- Draw lanes for each turtle.  
- Let the user choose how many turtles participate.  
- Display the winner on the screen instead of just printing it.  
