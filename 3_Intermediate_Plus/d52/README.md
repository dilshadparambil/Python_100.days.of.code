## Day 52: Instagram Followers Bot  
A Python bot that automates Instagram to log in, find a target account, and follow its followers.  

📄 [View Solution](solution.py) 📄 [View My Code](d52.py)  

---

### 🧠 Concepts Covered
- **Selenium WebDriver** for browser automation  
- **Instagram automation**: login, navigation, and interaction  
- **XPath and CSS Selectors** for locating dynamic web elements  
- **Scrolling automation** to load more followers  
- **Loops** for iterating over follower lists  
- **Explicit waits** (`WebDriverWait`) for synchronization  
- **Error handling** for pop-ups, login prompts, and rate limits  
- **Environment variables** to securely store credentials  
- **Headless browser execution** for efficiency  

---

### 📝 Instructions

#### 1. Install Dependencies
Install required Python packages:
```bash
pip install selenium
pip install python-dotenv
```
Download ChromeDriver (or relevant WebDriver) and ensure it's in your PATH.  

---

#### 2. Set Up Environment Variables
Create a `.env` file to store Instagram login credentials:
```env
INSTA_EMAIL=your_email
INSTA_PASSWORD=your_password
TARGET_ACCOUNT=account_to_scrape
```

---

#### 3. Launch Instagram and Log In
- Open Instagram login page:
```python
driver.get("https://www.instagram.com/accounts/login/")
```
- Locate username and password fields, fill in credentials, and log in:
```python
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(INSTA_EMAIL)
password_input.send_keys(INSTA_PASSWORD)
password_input.send_keys(Keys.ENTER)
```
- Use `WebDriverWait` to handle page load delays.

---

#### 4. Navigate to Target Account
- After login, navigate to the target account’s profile:
```python
driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
```
- Locate and click on the **followers** link to view their list.

---

#### 5. Scroll to Load Followers
- Scroll inside the modal to load all followers dynamically:
```python
scroll_box = driver.find_element(By.XPATH, "//div[@role='dialog']//div[@class='_aano']")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
```
- Repeat scrolling until all followers are loaded.

---

#### 6. Follow Each User
- Locate **Follow** buttons dynamically:
```python
follow_buttons = driver.find_elements(By.XPATH, "//button[text()='Follow']")
for button in follow_buttons:
    try:
        button.click()
        time.sleep(2)  # Pause to avoid bot detection
    except:
        continue
```
- Add random delays between clicks to simulate human behavior.

---

#### 7. Handle Pop-ups
- Use `try/except` to close pop-ups like "Confirm" or "Cancel":
```python
try:
    cancel_button = driver.find_element(By.XPATH, "//button[text()='Cancel']")
    cancel_button.click()
except:
    pass
```

---

#### 8. Run in Headless Mode (Optional)
```python
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

---

#### 9. Add Error Handling
- Handle:
  - Login verification pop-ups
  - Instagram temporary bans or CAPTCHAs
  - Internet issues  

---

💡 **Extra Challenges**:
- Build a **GUI dashboard** for follower stats.  
- Integrate a **scheduler** to run the bot daily.  
- Implement **like/comment automation** on recent posts.  
- Rotate **proxies** to avoid IP bans.  
