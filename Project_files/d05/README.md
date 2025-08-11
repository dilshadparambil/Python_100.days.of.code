### Day 5: Password Generator  
This program generates a secure password based on user preferences for letters, symbols, and numbers.  
You'll practice combining loops and lists to build both simple and randomized password generators.

📄 [View Solution](solution.py) 📄 [View My code](d5.py)  

#### 🧠 Concepts Covered
- `for` loops and `range()`  
- Code blocks and indentation  
- List creation and manipulation  
- Randomisation (`random` module)  
- User input handling  
- String joining and shuffling

#### 📝 Instructions
1. Ask the user:
   - How many **letters** they want in the password  
   - How many **symbols**  
   - How many **numbers**  
2. Generate the required number of characters using:
   - A list of letters (uppercase and lowercase)  
   - A list of symbols (`!`, `#`, `$`, etc.)  
   - A list of digits (`0-9`)  
3. Combine the selected characters into a password.

#### 🟢 Easy Version  
Generate the password in a fixed order:  
**`Letters → Symbols → Numbers`**

💡Example:  
```text
Input: 4 letters, 2 symbols, 3 numbers  
Output: fgdx$*924
```

Characters are grouped together by type.

#### 🔴 Hard Version  
Generate the password with **`randomized order`**:  
Characters are shuffled so there's **no pattern**.

💡Example:  
```text
Input: 4 letters, 2 symbols, 3 numbers  
Output: x$d24g*f9
```
You will need to:
- Combine all selected characters into one list  
- Use `random.shuffle()` to mix them  

---