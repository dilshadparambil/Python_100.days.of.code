### Day 13: Debugging Exercises  
A series of debugging challenges to identify and fix logical and syntax errors in given Python code.  
The day is divided into three separate problems, each focusing on fixing an existing buggy program.

📄 [View Odd or Even Question](d13a.py), [Solution](d13a_sol.py)  
📄 [View Leap Year Question](d13b.py), [Solution](d13b_sol.py)  
📄 [View FizzBuzz Question](d13c.py), [Solution](d13c_sol.py)   

#### 🧠 Concepts Covered
- Debugging techniques  
- Logical error identification and correction  
- Conditional statements (`if / elif / else`)  
- Modulo operator (`%`) for divisibility checks  
- Iteration with loops (`for` loops)  
- Testing code to ensure correctness

#### 📝 Instructions

##### 1️⃣ Debugging Odd or Even
- **Goal**: Read the given code and identify issues.  
- Fix the logic so that:
  - If the number is divisible by 2 → print `"This is an even number."`
  - Otherwise → print `"This is an odd number."`  
- Ensure the program runs without errors and passes all tests.

##### 2️⃣ Debugging Leap Year
- **Goal**: Identify and fix the issues in determining whether a year is a leap year.  
- **Correct leap year logic**:
  1. A year is a leap year if it is divisible by 4 **and** not divisible by 100.  
  2. Exception: If it is divisible by 400, it is still a leap year.  
- Example:
  - 2000 → Leap Year ✅  
  - 1900 → Not Leap Year ❌  
  - 1996 → Leap Year ✅  

##### 3️⃣ Debugging FizzBuzz
- **Goal**: Correct the logic to produce the proper FizzBuzz output.  
- Rules:
  - Print `"Fizz"` if the number is divisible by 3.  
  - Print `"Buzz"` if divisible by 5.  
  - Print `"FizzBuzz"` if divisible by both 3 and 5.  
  - Otherwise, print the number itself.  
- Loop from `1` to the user’s input number (`x`).  
- No copy-pasting from old solutions — fix the given buggy code.

💡 **Debugging Tips**:
- Use `print()` statements to trace variable values.  
- Check conditions order — specific cases (like divisible by both 3 & 5) should be checked before general cases.  
- Test with multiple inputs to confirm correctness.

---
