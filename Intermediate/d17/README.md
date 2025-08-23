## Day 17: Quiz Game  
A trivia quiz game that asks the user true/false questions and keeps track of the score.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d17.py)  

### 🧠 Concepts Covered
- **Classes and objects** for structuring a program  
- Using the `__init__` method to initialize object attributes  
- Defining and calling **attributes and methods**  
- Creating and managing **lists of objects**  
- Implementing **loops** for continuous gameplay  
- Importing from and organizing code across multiple Python files  
- Applying control flow for score tracking and quiz logic  

### 📝 Instructions
1. **Create the `Question` Class**  
   - Define a class named `Question`.  
   - Give it two attributes:  
     - `text` → the question string.  
     - `answer` → the correct answer (`"True"` or `"False"`).  
   - Use `__init__` to initialize these attributes when creating an object.  

2. **Build a Question Bank**  
   - Import `question_data` from **`data.py`**.  
   - Loop through the dictionary entries inside `question_data`.  
   - For each entry, create a new `Question` object with `text` and `answer`.  
   - Append each object to a `question_bank` list.  

3. **Create the `QuizBrain` Class**  
   - Attributes:  
     - `question_number` → keeps track of which question the user is on.  
     - `question_list` → stores the list of `Question` objects.  
     - `score` → keeps track of how many answers were correct.  
   - Methods:  
     - `still_has_questions()` → returns `True` if there are more questions left, otherwise `False`.  
     - `next_question()` → retrieves the current question, prompts the user for input, and calls `check_answer()`.  
     - `check_answer(user_answer, correct_answer)` → compares the user’s answer to the correct answer, updates score, and prints feedback.  

4. **Run the Quiz**  
   - Import the `QuizBrain` class and the `question_bank` list.  
   - Create an object of `QuizBrain`, passing in the `question_bank`.  
   - While `still_has_questions()` returns `True`:  
     - Call `next_question()` to display the next question.  
   - At the end, display the user’s **final score** and total questions answered.  

💡 **Extra Challenge**:  
- Add different question categories (e.g., science, history).  
- Fetch trivia questions dynamically from an API like [Open Trivia DB](https://opentdb.com/).  
- Add difficulty levels and track accuracy per category.  
