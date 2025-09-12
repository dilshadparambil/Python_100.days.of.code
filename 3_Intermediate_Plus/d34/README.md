## Day 34: Quizzler App (Trivia API)  
A GUI-based quiz application that fetches trivia questions from an online API and quizzes the user with instant feedback.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d34.py)  

### 🧠 Concepts Covered
- Object-Oriented Programming (OOP) with multiple classes  
- Tkinter for GUI design and user interaction  
- API requests and JSON responses  
- Handling external data with custom classes  
- Real-time feedback with color changes and delays  
- Maintaining and updating quiz score dynamically  

### 📝 Instructions
1. **Set up the Trivia API**  
   - Use the [Open Trivia Database API](https://opentdb.com/api_config.php) to fetch quiz questions in JSON format.  
   - Extract relevant data (question text and correct answer).  

2. **Create a `Question` class**  
   - Attributes: `text` and `answer`.  
   - Store each question as an instance of this class.  

3. **Build the `QuizBrain` class**  
   - Manage the quiz logic including question progression and score tracking.  
   - Methods:  
     - `still_has_questions()` → check if there are remaining questions.  
     - `next_question()` → get the next question and update progress.  
     - `check_answer(user_answer)` → verify the user’s answer and update the score.  

4. **Design the GUI (`ui.py`)**  
   - Use Tkinter to create the main window with a canvas for displaying questions.  
   - Add **True** and **False** buttons for user responses.  
   - Display the score at the top of the window.  

5. **Connect GUI with `QuizBrain`**  
   - When a user clicks **True** or **False**, call `check_answer()` from `QuizBrain`.  
   - Provide visual feedback:  
     - Green background if correct.  
     - Red background if incorrect.  
   - Wait briefly before showing the next question using `after()` method.  

6. **Handle End of Quiz**  
   - When all questions are finished, disable the buttons.  
   - Display a message like *“You’ve reached the end of the quiz”* on the canvas.  

💡 **Extra Challenge**:  
- Add a dropdown to select quiz categories and difficulty from the API.  
- Implement a timer for each question.  
- Save high scores to a file and display them in the UI.  
