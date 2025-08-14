## Day 17: Quiz Game  
A console-based quiz game that tests the user’s knowledge with multiple-choice True/False questions.  
Questions are fetched from a data source and handled using OOP for better structure and scalability.

📄 [View Solution](solution/solution.py) 📄 [View My code](my_code/d17.py)   

### 🧠 Concepts Covered
- Object-Oriented Programming (OOP)  
- Creating and using classes (`Question`, `QuizBrain`)  
- Initializing objects with `__init__()`  
- Lists and iteration to store and process questions  
- Conditional statements for answer checking  
- Incremental scoring and game loop control  
- Data management from an external source file (`data.py`)


### 📝 Instructions

1. **Question Data**  
   - Store quiz questions and answers in a Python dictionary list (in `data.py`).  
   - Each dictionary contains `"text"` and `"answer"` keys.

2. **Question Model**  
   - Create a `Question` class with:
     - Attributes: `text` (str), `answer` (str)  
     - Constructor to initialize question data.

3. **Quiz Brain**  
   - Create a `QuizBrain` class to control quiz flow with methods:
     - `still_has_questions()` → Checks if there are more questions left.  
     - `next_question()` → Displays the next question and collects user input.  
     - `check_answer(user_answer)` → Compares answer, updates score, and gives feedback.

4. **Game Loop**  
   - Import `Question` and `QuizBrain`.  
   - Convert `data.py` into a list of `Question` objects.  
   - Keep asking questions until no more remain.  
   - At the end, display the final score.

5. **Scoring System**  
   - Keep track of the user’s score as they answer.  
   - Display current score after each question.


💡 **Extra Challenge**:
- Add more question types (Multiple Choice).  
- Randomize question order.  
- Fetch data from an API for dynamic quizzes.  
- Add a difficulty level system.
