## Day 25: U.S. States Game  
A fun geography quiz game where the user guesses U.S. state names, and correct guesses appear on a blank U.S. map until all 50 states are guessed or the game ends.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d25.py) 

### 🧠 Concepts Covered
- Reading and exporting data using **CSV files**  
- Using **Pandas** for data handling and filtering  
- `pandas.item()` method to extract values from a DataFrame  
- Implementing **loops** for repeated guessing until the game ends  
- Using **turtle graphics** to write text on a map dynamically  

### 📝 Instructions
1. **Set up the game screen**  
   - Use the `turtle` module to display a blank U.S. map as the background.  
   - Give the screen a title such as `"U.S. States Game"`.  

2. **Load state data**  
   - Read the `50_states.csv` file using **Pandas**.  
   - Store the state names and their corresponding `(x, y)` coordinates from the CSV.  

3. **Prompt the user for guesses**  
   - Use `turtle.textinput()` to ask the user:  
     `"What's another state's name?"`.  
   - Convert the user’s input to **title case** so it matches the formatting of the data.  

4. **Check the guess**  
   - If the guessed state is one of the 50 states:  
     - Retrieve its `(x, y)` coordinates from the DataFrame using `pandas.item()`.  
     - Create a turtle that writes the state name at the correct location on the map.  
   - If the guess is incorrect, do nothing and prompt the user again.  

5. **Keep track of guesses**  
   - Maintain a list of all correctly guessed states.  
   - Update the score with each correct guess.  

6. **Loop until game ends**  
   - Continue prompting the user for guesses until:  
     - All 50 states are guessed (the user wins), or  
     - The user types `"Exit"`.  

7. **Handle the “Exit” case**  
   - When the user types `"Exit"`, generate a CSV file containing the states they missed.  
   - Save this as `"states_to_learn.csv"` so the user can practice later.  

8. **Show progress**  
   - Keep updating the score in the input prompt to reflect how many states the user has guessed (e.g., `20/50 States Correct`).  
   - Give the user visual feedback directly on the map as they guess more states.  

💡 Extra Challenge:  
- Add a timer to make the game more competitive.  
- Randomize prompts or give hints for missed states.  
- Expand the game for **other countries or continents** by using different map images and CSV data.  
