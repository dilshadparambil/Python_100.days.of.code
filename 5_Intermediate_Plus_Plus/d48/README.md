## Day 48: Game Playing Bot  
An automation bot built using Selenium to play and interact with a browser-based game automatically.
This project focuses on automating repetitive actions, detecting elements dynamically, and implementing loops and delays to create a fully functional game bot.

📄 [View Solution](solution.py) 📄 [View My Code](d48.py) 📄 [Game link](https://ozh.github.io/cookieclicker/).  

---

### 🧠 Concepts Covered
- **Selenium WebDriver**: Automating browser actions  
- **XPath & CSS Selectors**: Locating elements dynamically  
- **Browser automation**: Opening URLs, clicking buttons, and interacting with game elements  
- **Loops for automation**: Automating repetitive actions  
- **`time.sleep()` and waits**: Adding delays for realistic interactions  
- **Conditional logic**: Detecting elements and responding to changes in the game  
- **Error handling**: Handling dynamic page changes gracefully  

---

### 📝 Instructions

#### 1. Set Up the Development Environment
- Install required libraries:  
  ```bash
  pip install selenium
  ```
- Download and configure a compatible **WebDriver** (e.g., ChromeDriver or GeckoDriver).  
- Import necessary modules:  
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  import time
  ```

#### 2. Initialize WebDriver
- Create a new browser instance:
  ```python
  driver = webdriver.Chrome()
  driver.get("URL_OF_THE_GAME")
  ```
- Set up window size and optionally configure options to speed up execution.

---

#### 3. Locate Key Game Elements
- Identify essential game elements using:
  - `driver.find_element(By.ID, "element_id")`
  - `driver.find_element(By.XPATH, "xpath_here")`
  - `driver.find_element(By.CSS_SELECTOR, ".class_name")`
- Store these elements in variables for quick access.

---

#### 4. Automate Game Actions
- Use loops to repeatedly interact with the game:
  ```python
  while True:
      game_element.click()
      # Optional logic for upgrades or bonuses
  ```
- Continuously monitor for:
  - Score updates
  - Bonuses
  - Level-up opportunities

---

#### 5. Add Conditional Logic
- Write logic to check when:
  - A new upgrade is available  
  - A bonus element appears  
  - A game-over or reset condition is triggered  

---

#### 6. Implement Upgrades and Bonuses
- Add checks to see if certain elements are enabled:
  ```python
  if upgrade.is_enabled():
      upgrade.click()
  ```
- Automate purchasing or claiming bonuses.

---

#### 7. Optimize the Loop
- Use `time.sleep()` or WebDriver waits to avoid overwhelming the browser:
  ```python
  time.sleep(0.1)
  ```

---

#### 8. Exit or Stop the Bot
- Allow the script to end gracefully after a set time or a game condition.

---

💡 **Extra Challenges**:
- Add logging to track bot actions and progress.  
- Use `WebDriverWait` and `expected_conditions` for more dynamic interaction.  
- Create a modular structure with separate functions for initialization, upgrades, and gameplay.  
- Add multi-threading for advanced bot control.

