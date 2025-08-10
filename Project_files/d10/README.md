### Day 10: Calculator  
A simple interactive calculator that can perform addition, subtraction, multiplication, and division.  
This project introduces **functions with outputs**, function references in dictionaries, and recursive program flow.

📄 [View the code](Project_files/d10/solution.py) [🔼 Back to Top](#-table-of-contents)

#### 🧠 Concepts Covered
- Functions with outputs (`return`)  
- Storing functions as dictionary values  
- Using dictionary keys to trigger operations  
- Recursion for program restarts  
- Docstrings for function documentation

#### 📝 Instructions

1. **Write the core math functions**:
   - `add(n1, n2)`
   - `subtract(n1, n2)`
   - `multiply(n1, n2)`
   - `divide(n1, n2)`

2. **Create an operations dictionary**:
   ```python
   operations = {
       "+": add,
       "-": subtract,
       "*": multiply,
       "/": divide
   }
   ```

3. **Basic program flow**:
   - Ask the user for the **first number**.
   - Ask the user to choose an **operator** (`+`, `-`, `*`, `/`).
   - Ask for the **second number**.
   - Perform the calculation using the operations dictionary:
   ```python
   result = operations["*"](n1=4, n2=8)
   ```
   - Display the result.

4. **Chaining calculations**:
   - Ask if the user wants to continue with the previous result.
   - If **yes** → Use the result as the first number and repeat.
   - If **no** → Restart the calculator from scratch.

5. **Add a logo**:
   - Import and display the ASCII art logo from `art.py` at the start.

💡 **Hints**:
   - Use `float()` to handle decimal inputs.
   - Recursive function calls can restart the calculator cleanly without a `while` loop.
   - Write **docstrings** for each function to explain its purpose.

---