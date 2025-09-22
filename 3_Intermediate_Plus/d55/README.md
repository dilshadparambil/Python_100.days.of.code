## Day 55: Higher Lower URLs (Flask Project)  
A simple Flask web app where the user guesses a number via URL routing. The app provides feedback (too high, too low, or correct) directly in the browser.  

📄 [View Solution](solution.py) 📄 [View My Code](d55.py)  

---

### 🧠 Concepts Covered
- **Flask basics** → Creating a web server with Python  
- **URL routing with decorators (`@app.route`)**  
- **Dynamic URL paths** → Capturing user input from the URL  
- **Conditional logic** for comparisons  
- **Returning HTML responses** directly from Flask routes  
- **Random number generation** with `random.randint()`  

---

### 📝 Instructions

#### 1. Install and Import Flask
```bash
pip install flask
```
```python
from flask import Flask
import random
```

---

#### 2. Set up Flask App
Initialize the app:
```python
app = Flask(__name__)
```

---

#### 3. Generate a Random Number
At the start of the program, generate a random number between 0–9:
```python
number_to_guess = random.randint(0, 9)
```

---

#### 4. Create the Home Route
Display a welcome message and game instructions:
```python
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"
```

---

#### 5. Create a Dynamic Route for Guesses
Capture guesses directly from the URL:
```python
@app.route("/<int:guess>")
def check_guess(guess):
    if guess < number_to_guess:
        return "<h1 style='color:blue'>Too low, try again!</h1>"
    elif guess > number_to_guess:
        return "<h1 style='color:red'>Too high, try again!</h1>"
    else:
        return "<h1 style='color:green'>Correct! You found me!</h1>"
```

---

#### 6. Run the Flask App
```python
if __name__ == "__main__":
    app.run(debug=True)
```

---

#### 7. Play the Game
- Open your browser and go to:  
  - `http://127.0.0.1:5000/` → instructions  
  - `http://127.0.0.1:5000/5` → guess number 5  

---

💡 **Extra Challenge**:  
- Add **GIFs or images** (too high, too low, correct).  
- Expand range to 0–20 or more.  
- Add difficulty levels with query parameters.  

---  
