## Day 26: NATO Alphabet Project  
A program that converts a user-inputted word into its NATO phonetic alphabet equivalent using dictionary comprehension and pandas.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d26.py)  

### 🧠 Concepts Covered
- List comprehensions for creating lists in a single line  
- Dictionary comprehensions to quickly map letters to their phonetic codes  
- Iterating through a DataFrame with `iterrows()` in pandas  
- Error handling for invalid inputs (e.g., numbers or symbols)  
- Breaking down a word into individual letters and mapping them to dictionary values  

### 📝 Instructions
1. **Load the Data**  
   - Use pandas to read the `nato_phonetic_alphabet.csv` file.  
   - The CSV contains two columns: `letter` and `code`.  

2. **Create a Dictionary with Dictionary Comprehension**  
   - Convert the DataFrame into a dictionary where each letter maps to its NATO code.  
   - Example:  
     ```python
     phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
     ```
   - The dictionary should look like:  
     ```python
     {"A": "Alfa", "B": "Bravo", "C": "Charlie", ...}
     ```

3. **Ask the User for Input**  
   - Prompt the user to type a word.  
   - Convert the input to uppercase so it matches the dictionary keys.  

4. **Generate the NATO Phonetic List**  
   - Use a **list comprehension** to iterate through each letter in the input word.  
   - Replace each letter with its corresponding phonetic code from the dictionary.  
   - Example:  
     ```
     Input: "DOG"
     Output: ["Delta", "Oscar", "Golf"]
     ```

5. **Handle Invalid Inputs**  
   - If the user enters numbers or symbols, the program should prompt them again.  
   - Example: If the user types `HELLO123`, it should display an error and re-ask for input.  

6. **Display the Final Result**  
   - Print the generated list of NATO codes for the user.  
   - Example Output:  
     ```
     Enter a word: DOG  
     ['Delta', 'Oscar', 'Golf']
     ```

💡 **Extra Challenge**:  
- Try extending the project by allowing the user to input multiple words (e.g., a sentence).  
- Store the phonetic output in a file so it can be reused later.  
