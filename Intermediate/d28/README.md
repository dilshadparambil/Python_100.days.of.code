## Day 28: Pomodoro Timer (GUI)  
A productivity app based on the Pomodoro Technique, built with Tkinter. The timer alternates between focused work sessions and short/long breaks, helping improve concentration and time management.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d28.py)  

### 🧠 Concepts Covered
- Tkinter GUI (labels, buttons, canvas widgets)  
- Dynamic typing in Python  
- Tkinter Canvas for drawing and updating UI elements (timer text, images)  
- `window.after()` method for scheduling function calls after a delay  
- Loops and conditional logic for session switching  
- Resetting UI state programmatically  

### 📝 Instructions

1. **Set up the Tkinter Window**  
   - Import `tkinter` and create the main app window.  
   - Configure padding, background color, and title.  

2. **Add a Timer Label**  
   - Create a label at the top displaying "Timer".  
   - Change its text dynamically based on session type ("Work", "Break").  

3. **Add a Canvas Widget**  
   - Place an image (e.g., a tomato icon) using `Canvas.create_image()`.  
   - Add a text element to the canvas for showing the countdown timer.  

4. **Add Start and Reset Buttons**  
   - Start button → triggers the timer sequence.  
   - Reset button → stops the timer and resets everything (labels, countdown, marks).  

5. **Implement Timer Logic**  
   - Use global variables to track repetitions (work sessions, short breaks, long breaks).  
   - Define constants for session lengths (e.g., 25 minutes for work, 5 minutes for break).  
   - Switch between sessions depending on repetition count.  

6. **Countdown Function**  
   - Define a recursive countdown using `window.after(1000, function)`.  
   - Update the canvas timer text each second.  
   - When countdown reaches zero, start the next session automatically.  

7. **Session Switching Rules**  
   - Odd sessions → Work (25 min).  
   - Even sessions (except 8th) → Short Break (5 min).  
   - Every 8th session → Long Break (20 min).  

8. **Progress Tracking**  
   - After each work session, add a ✓ checkmark under the timer to track completed Pomodoros.  

9. **Run the App**  
   - Call `window.mainloop()` to keep the GUI running.  

💡 **Extra Challenge**:  
- Add sound notifications when a session ends.  
- Let the user customize work/break durations.  
- Save session history to a file for tracking productivity over time.  
