## Day 19: Turtle Racing  
A fun Python program that simulates a turtle race. Multiple turtles line up at the start and race across the screen, with the user betting on which turtle will win.

📄 [View Solution](solution.py) 📄 [View My Code](d18.py)  

### 🧠 Concepts Covered
- More advanced turtle graphics  
- Event listeners for user interaction  
- Higher-order functions (passing functions as arguments)  
- Managing state in a game loop  
- Creating and handling multiple instances of an object (`Turtle`)  

### 📝 Instructions
1. Import the `turtle` and `random` modules.  
2. Set up the race screen with `Screen()` and configure its dimensions.  
3. Prompt the user to place a bet on which turtle color will win.  
4. Create multiple turtle racers:  
   - Initialize turtles with different colors.  
   - Position them at the starting line.  
5. Start the race using a loop:  
   - Move each turtle forward by a random distance.  
   - Check after each step if a turtle has crossed the finish line.  
6. Compare the winning turtle’s color with the user’s bet and display the result.  
7. Keep the screen open until the user clicks to exit.  

💡 **Extra Challenge**:
- Allow multiple bets or custom bet amounts.  
- Add a finish line graphic.  
- Implement a restart option without closing the program.  
