## Day 50: Automated Rock-Paper-Scissors Bot  
A Python bot that automates playing **Rock-Paper-Scissors** on a web-based game platform using **Selenium WebDriver**.  
The bot identifies the opponent's choice and dynamically selects the winning move.

📄 [View Solution](solution.py) 📄 [View My Code](d50.py)  

---

### 🧠 Concepts Covered
- **Selenium WebDriver** for browser automation  
- **XPath and CSS Selectors** for dynamic element interaction  
- **Web scraping** text and image-based game choices  
- **Decision-making algorithms** to select winning moves  
- **Explicit waits** (`WebDriverWait`) for dynamic page elements  
- **Loops for continuous gameplay** automation  
- **Screenshot or OCR integration** for detecting image-based choices  
- **Error handling** for unexpected elements or page changes  
- **Environment setup** for browser drivers  

---

### 📝 Instructions

#### 1. Install Dependencies
- Install Selenium:
  ```bash
  pip install selenium
  ```
- Download and set up ChromeDriver (or the driver for your preferred browser).
- Verify browser compatibility with the Selenium WebDriver version.

---

#### 2. Launch Game Page
- Import required libraries and start a browser session:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By

  driver = webdriver.Chrome()
  driver.get("ROCK_PAPER_SCISSORS_GAME_URL")
  ```

---

#### 3. Detect Opponent's Choice
- Locate the element that displays the opponent’s move (text or image):
  ```python
  opponent_move = driver.find_element(By.ID, "opponent_choice").text
  ```

---

#### 4. Decide the Winning Move
- Use a dictionary or logic mapping to decide your response:
  ```python
  beats = {
      "rock": "paper",
      "paper": "scissors",
      "scissors": "rock"
  }
  my_move = beats[opponent_move]
  ```

---

#### 5. Automate Clicks
- Locate and click your chosen move button dynamically:
  ```python
  button = driver.find_element(By.XPATH, f"//button[text()='{my_move.capitalize()}']")
  button.click()
  ```

---

#### 6. Add Waits for Page Updates
- Use explicit waits to ensure the next round loads correctly:
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.ID, "next_round"))
  )
  ```

---

#### 7. Loop for Multiple Rounds
- Wrap gameplay logic in a loop to automate multiple matches:
  ```python
  while True:
      # Detect opponent move
      # Decide and click winning move
      # Wait for round to update
  ```

---

#### 8. Error Handling
- Add `try/except` blocks to handle:
  - Missing or dynamic elements
  - Unexpected DOM changes
  - Page load timeouts

---

#### 9. Optimization (Optional)
- Run in **headless mode** for faster execution:
  ```python
  from selenium.webdriver.chrome.options import Options
  options = Options()
  options.add_argument("--headless")
  driver = webdriver.Chrome(options=options)
  ```
- Add **logging** for round results and win/loss tracking.

---

💡 **Extra Challenges**:
- Add a **GUI dashboard** to display your win rate dynamically.  
- Integrate **image recognition** with `pytesseract` for image-based RPS games.  
- Use **AI** or reinforcement learning to detect game patterns.  
- Schedule bot runs to automatically play at certain times.

