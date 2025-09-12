## Day 30: Password Manager (GUI App with Search)  
An upgraded version of the password manager that not only generates and saves passwords but also allows users to search for saved credentials using a website name. Data is stored in a JSON file for structured management.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](d30.py)  

### 🧠 Concepts Covered
- Tkinter GUI (labels, entries, buttons, messageboxes)  
- JSON file handling with `load()`, `dump()`, and `update()`  
- Error handling with `try`, `except`, `else`, and `finally`  
- Searching and retrieving data from JSON files  
- Exception handling for missing files or invalid keys  

### 📝 Instructions

1. **Set up the Tkinter Window**  
   - Create the main app window with Tkinter.  
   - Add padding, a title, and optional canvas/logo at the top.  

2. **Create Labels and Entry Fields**  
   - Add input fields for:  
     - **Website**  
     - **Email/Username**  
     - **Password**  
   - Place them neatly using `grid()` layout.  
   - Set `.focus()` to the Website field for convenience.  

3. **Password Generator Button**  
   - Add a button to generate a secure random password.  
   - Auto-fill the password field with the generated password.  
   - Copy the generated password to the clipboard for easy use.  

4. **Save Passwords to JSON File**  
   - When "Add" is clicked:  
     - Validate that fields are not empty.  
     - Open or create a JSON file (`data.json`).  
     - Use `json.load()` to read existing data (inside `try-except` for FileNotFound).  
     - Update the dictionary with new data using `update()`.  
     - Save updated data back to the file with `json.dump()`.  
   - Example structure of `data.json`:  
     ```json
     {
       "example.com": {
         "email": "user@example.com",
         "password": "password123"
       }
     }
     ```  

5. **Search for Saved Credentials**  
   - Add a "Search" button next to the Website entry field.  
   - On click, retrieve the website input.  
   - Open `data.json` with `json.load()`.  
   - If the website exists, show the email and password in a `messagebox`.  
   - If not found, show an error message.  
   - Handle errors if `data.json` does not exist using `try-except`.  

6. **Error Handling with try-except-else-finally**  
   - Use `try` for reading JSON files.  
   - Catch `FileNotFoundError` and create a new file if it doesn’t exist.  
   - Use `else` to process data when no errors occur.  
   - Use `finally` for cleanup actions (if needed).  

7. **Run the App**  
   - Start the Tkinter main event loop with `window.mainloop()`.  

💡 **Extra Challenge**:  
- Add a "Delete" button to remove saved credentials.  
- Add a "Show All" feature to list all saved websites.  
- Encrypt passwords before saving for more security.  
