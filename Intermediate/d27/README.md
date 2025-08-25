## Day 27: Mile to Km Converter (GUI)  
A simple GUI app that converts miles to kilometers using Tkinter.  

📄 [View My Code](d27.py)  

### 🧠 Concepts Covered
- Creating graphical user interfaces (GUIs) with Tkinter  
- Configuring labels, entry widgets, and buttons  
- Using **default arguments** in functions  
- Understanding `*args` (arbitrary positional arguments)  
- Understanding `**kwargs` (arbitrary keyword arguments)  
- Handling user input and updating widgets dynamically  

### 📝 Instructions
1. **Set up the Tkinter Window**  
   - Import the `tkinter` module.  
   - Create the main window using `Tk()`.  
   - Add padding and set a descriptive window title (e.g., "Mile to Km Converter").  

2. **Create an Input Field (Entry Widget)**  
   - Add an entry box where the user can type the number of miles.  
   - Use `.grid(column=1, row=0)` (or another layout) to position it in the GUI.  

3. **Add Labels for Context**  
   - Create a label `"Miles"` next to the input box.  
   - Create another label `"is equal to"` to describe the conversion.  
   - Add a label `"Km"` next to the result.  
   - Arrange them with `.grid()` so the GUI looks clean and intuitive.  

4. **Add a Result Label**  
   - Create a label initialized with `"0"`.  
   - This label will update dynamically to show the converted kilometers.  
   - Place it in the correct row and column next to `"is equal to"`.  

5. **Create a Button**  
   - Add a button labeled `"Calculate"`.  
   - Use `.grid()` to position it below the entry field.  
   - Bind the button to a function that runs the conversion logic when clicked.  

6. **Write the Conversion Function**  
   - Inside the function, use `entry.get()` to retrieve the miles value as a string.  
   - Convert it to a float or int.  
   - Apply the formula:  
     ```python
     km = miles * 1.609
     ```  
   - Update the result label with the converted value, rounded to 2 decimal places.  

7. **Run the Application**  
   - Start the Tkinter main loop with `window.mainloop()`.  
   - This keeps the GUI running and responsive until the user closes it.  

💡 **Extra Challenge**:  
- Experiment with `*args` and `**kwargs` in your button callback to understand how Tkinter passes event arguments.  
- Add input validation to handle invalid inputs (like text instead of numbers).  
- Customize fonts, padding, and colors for a better user experience.  
