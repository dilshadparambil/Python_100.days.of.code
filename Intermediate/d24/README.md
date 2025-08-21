## Day 24: Mail Merge  
A program that automatically generates personalized letters by merging a template with a list of names.

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d24.py)  

### 🧠 Concepts Covered
- Working with files and directories  
- Opening, closing, reading, and writing files  
- Using `str.replace()` to substitute text in templates  
- Using `str.strip()` to clean unwanted whitespace/newlines  
- Reading multiple lines with `file.readlines()`  

### 📝 Instructions
1. Open the file containing the list of names (e.g., `invited_names.txt`).  
2. Read all the names into a list using `readlines()`.  
3. Open the letter template file (e.g., `starting_letter.txt`).  
4. For each name in the names list:  
   - Strip unwanted characters (like `\n`) using `strip()`.  
   - Replace the placeholder `[name]` in the template with the actual name using `replace()`.  
   - Save the personalized letter into the `Output` folder with a filename like `letter_for_<name>.txt`.  

💡 **Extra Challenge**:  
- Allow the user to input their own template file.  
- Add support for bulk email sending instead of letters.  
