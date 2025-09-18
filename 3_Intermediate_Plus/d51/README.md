## Day 51: Internet Speed Complaining Twitter Bot  
A Python bot that automatically checks your internet speed and tweets a complaint to your ISP if the speed is below your promised plan.  

📄 [View Solution](solution.py) 📄 [View My Code](d51.py)  

---

### 🧠 Concepts Covered
- **Selenium WebDriver** for browser automation  
- **Automating internet speed tests** using [speedtest.net](https://www.speedtest.net/)  
- **Extracting dynamic data** with XPath and CSS Selectors  
- **Twitter automation**: Logging in and tweeting  
- **Explicit waits** (`WebDriverWait`) for reliable element interactions  
- **Environment variables** for secure credential management  
- **Error handling** for dynamic pages and login verification  
- **Headless browsing** for faster execution  

---

### 📝 Instructions

#### 1. Install Dependencies
Install required Python packages:
```bash
pip install selenium
pip install python-dotenv
```
Download ChromeDriver (or relevant driver) and ensure it's in your PATH.  

---

#### 2. Set Up Environment Variables
Create a `.env` file to securely store credentials:
```env
PROMISED_DOWN=150
PROMISED_UP=50
TWITTER_EMAIL=your_email
TWITTER_PASSWORD=your_password
TWITTER_USERNAME=your_username
```

---

#### 3. Automate Internet Speed Test
- Use Selenium to open [speedtest.net](https://www.speedtest.net/).
- Click the **Go** button to start the test:
```python
go_button = driver.find_element(By.CLASS_NAME, "start-text")
go_button.click()
```
- Wait for test completion and scrape download/upload speeds:
```python
download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text
```

---

#### 4. Compare with Promised Speeds
Convert scraped strings to floats and compare with promised speeds from `.env`.  

---

#### 5. Automate Twitter Login
- Open Twitter and locate input fields for username, password, and login buttons:
```python
driver.get("https://twitter.com/login")
username = driver.find_element(By.NAME, "text")
password = driver.find_element(By.NAME, "password")
```
- Use `WebDriverWait` for dynamic login elements.  

---

#### 6. Compose and Send Tweet
- Create a complaint tweet with f-strings:
```python
tweet = f"Hey ISP, why is my download speed {download_speed}Mbps and upload speed {upload_speed}Mbps when I pay for {PROMISED_DOWN}/{PROMISED_UP}Mbps?"
```
- Automate tweet posting by locating the tweet box and **Tweet** button.  

---

#### 7. Add Loops and Error Handling
- Add try/except blocks for:
  - Speedtest failures
  - Login verification errors
  - Rate limits  

---

#### 8. Run in Headless Mode (Optional)
```python
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

---

#### 9. Schedule the Bot
- Use **cron jobs** (Linux/Mac) or **Task Scheduler** (Windows) to run the bot at intervals.  

---

💡 **Extra Challenges**:
- Log all test results to a CSV or Google Sheets.  
- Send complaints via email or WhatsApp in addition to Twitter.  
- Add automatic retry if Twitter login fails.  
- Implement proxy rotation to bypass rate limits.  
