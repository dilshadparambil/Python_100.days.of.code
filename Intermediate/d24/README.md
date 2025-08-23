## Day 24: Mail Merge  
A program that automatically generates personalized letters by merging a template with a list of names.

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d24.py)  

### 🧠 Concepts Covered
- Working with files and directories (`with open()`)  
- Opening, closing, reading, and writing files  
- Using `str.replace()` to substitute text in templates  
- Using `str.strip()` to clean unwanted whitespace/newlines  
- Reading multiple lines with `file.readlines()`  
- Automating repetitive tasks with loops  

### 📝 Instructions
1. **Prepare your input files**  
   - Create a file called `invited_names.txt` containing the list of names (one per line).  
   - Create a letter template file called `starting_letter.txt` with a placeholder like:  
     ```
     Dear [name],
     You are invited to my birthday party...
     ```  

2. **Read the list of names**  
   - Open `invited_names.txt` using `with open()`.  
   - Read all lines into a list with `.readlines()`.  

3. **Read the template**  
   - Open `starting_letter.txt` and store its content as a string.  

4. **Generate personalized letters**  
   - Loop through the list of names.  
   - Use `.strip()` to remove newline characters from each name.  
   - Replace the `[name]` placeholder in the template with the actual name using `.replace()`.  

5. **Save the output files**  
   - Write the customized letter to a new file inside an `Output` folder.  
   - Use a naming convention such as:  
     ```
     letter_for_<name>.txt
     ```  

6. **Check results**  
   - Verify that each file has been generated correctly with the recipient’s name.  

💡 **Extra Challenge**:  
- Allow the user to select a custom template file at runtime.  
- Add support for bulk email sending instead of saving to text files.  
- Save letters in different formats (e.g., `.docx` or `.pdf`).  
