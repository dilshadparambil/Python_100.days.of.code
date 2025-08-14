## Day 8: Caesar Cipher  
Build your own text encryption and decryption tool using Caesar Cipher logic!  
This project introduces function inputs, parameter handling, and simple text transformations.

📄 [View Solution](solution.py) 📄 [View My code](d8.py)  

### 🧠 Concepts Covered
- Functions with inputs  
- Parameters and arguments  
- Positional vs keyword arguments  
- Indexing in lists  
- String and character manipulation  
- Looping through strings  
- Preserving non-alphabet characters  
- Creating reusable logic with control flow

### 📝 Instructions

1. Create a function called `encrypt()` that takes `original_text` and `shift_amount` as parameters.
   - Shift each letter in the text **forwards** by the `shift_amount`.
   - Use `alphabet.index()` to find positions.
   - Handle wrap-around from `'z'` to `'a'`.
   - Example:  
     ```python
     plain_text = "hello"
     shift_amount = 1
     # Output: ifmmp
     ```

2. Create a function called `decrypt()` that:
   - Shifts each letter **backwards** by the `shift_amount`.
   - Reverses the encryption process.

3. Combine both `encrypt()` and `decrypt()` into a single function called `caesar()`.
   - Add a `direction` input to determine which action to take.
   - Call this function using user inputs for `direction`, `text`, and `shift`.

4. Handle edge cases:
   - If the user enters numbers, symbols, or spaces, preserve them in the result.
     - Example:  
       ```text
       original_text = "meet me at 3!"
       cipher_text = "xxxx xx xx 3!"  # letters shifted, digits/symbols untouched
       ```

5. Add a restart option:
   - Ask the user if they want to encode/decode another message:
     ```text
     Type 'yes' if you want to go again. Otherwise, type 'no'.
     ```

💡 **Bonus Tips**:  

- Use `modulus (%)` to wrap around the alphabet if shifting past `'z'`.  
- Convert text to lowercase before processing for consistency.  
- Use a `while` loop to allow restarting the cipher repeatedly.

---