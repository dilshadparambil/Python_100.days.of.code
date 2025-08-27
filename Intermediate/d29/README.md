## Day 29: Password Manager (GUI App)  
A simple password manager built with Tkinter that allows users to generate strong random passwords, save them securely, and copy them to the clipboard for easy use.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d29.py)  

### 🧠 Concepts Covered
- Tkinter GUI layout and widgets  
- `grid()` with `columnspan` and `sticky` for better widget alignment  
- `.focus()` to auto-select the first entry field  
- Using `messagebox` for user interactions (`askokcancel`, `showerror`)  
- Copying text to the clipboard with `pyperclip.copy()`  
- File handling for saving credentials (website, email/username, password)  

### 📝 Instructions

1. **Set up the Tkinter Window**  
   - Create the main window with Tkinter.  
   - Add padding and set a title for the window.  

2. **Add a Logo/Image (Optional)**  
   - Use `Canvas` to display a logo at the top of the app.  

3. **Create Labels and Entry Fields**  
   - Add labels for "Website", "Email/Username", and "Password".  
   - Use `Entry` widgets for user input.  
   - Set `.focus()` on the Website field so it is active when the app starts.  
   - Use `grid()` with `columnspan` and `sticky` for proper placement.  

4. **Add a Password Generator Button**  
   - Create a button that generates a random secure password.  
   - Insert the generated password into the password field automatically.  
   - Use `pyperclip.copy()` to copy the generated password to the clipboard.  

5. **Add Save Button**  
   - When clicked, validate inputs (website, email, password should not be empty).  
   - If fields are empty, show an error using `messagebox.showerror()`.  
   - Otherwise, show a confirmation popup with `messagebox.askokcancel()`.  
   - If confirmed, append the credentials to a text file (e.g., `data.txt`).  
   - Clear the website and password fields after saving.  

6. **Password Storage Format**  
   - Save credentials in a text file in this format:  
     ```
     Website | Email | Password
     ```  

7. **Run the App**  
   - Start the Tkinter main event loop with `window.mainloop()`.  

💡 **Extra Challenge**:  
- Add a search feature to look up saved credentials.  
- Encrypt stored passwords for extra security.  
- Add a “Copy Email” button similar to the password copy functionality.  
