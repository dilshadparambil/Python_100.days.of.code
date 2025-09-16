## Day 49: Automated Gym Workout Booking  
A Python automation script using **Selenium WebDriver** to automatically book gym workout sessions on a fitness platform.  
This project focuses on automating login, navigating through booking pages, and selecting available time slots.

📄 [View Solution](solution.py) 📄 [View My Code](d49.py)  

---

### 🧠 Concepts Covered
- **Selenium WebDriver** for browser automation  
- **Environment variables** for secure login credentials  
- **XPath & CSS Selectors** for dynamic element selection  
- **Automated form filling** for login details  
- **Navigation automation** for page interactions  
- **Loops and conditions** for booking slots dynamically  
- **Explicit waits** (`WebDriverWait`) for elements to load  
- **Error handling** for unexpected UI changes  
- **Headless browser mode** for faster execution  

---

### 📝 Instructions

#### 1. Install Dependencies
- Install Selenium:
  ```bash
  pip install selenium
  ```
- Download and set up ChromeDriver (or a driver for your preferred browser).  
- Store your **username and password** as environment variables for security.

---

#### 2. Initialize WebDriver
- Create a new browser instance:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By

  driver = webdriver.Chrome()
  driver.get("GYM_PORTAL_URL")
  ```

---

#### 3. Automate Login
- Locate the username and password input fields using `By.ID`, `By.NAME`, or XPath.  
- Fill in credentials:
  ```python
  username = driver.find_element(By.ID, "username_field")
  password = driver.find_element(By.ID, "password_field")

  username.send_keys(USERNAME)
  password.send_keys(PASSWORD)
  ```
- Click the **Login** button.

---

#### 4. Navigate to Booking Page
- Use `driver.find_element()` with `By.LINK_TEXT` or `By.XPATH` to locate navigation links.  
- Click to reach the workout booking section.

---

#### 5. Select a Workout Session
- Identify available time slots:
  ```python
  slot = driver.find_element(By.XPATH, "//button[contains(text(), 'Available')]")
  slot.click()
  ```
- Use conditions to check if slots are available before attempting to book.

---

#### 6. Confirm the Booking
- Click the confirmation button and wait for success message:
  ```python
  confirm = driver.find_element(By.ID, "confirm_button")
  confirm.click()
  ```

---

#### 7. Add Explicit Waits
- Implement `WebDriverWait` to ensure elements load properly:
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "booking_confirmation"))
  )
  ```

---

#### 8. Add Error Handling
- Wrap actions in `try/except` blocks to handle:
  - Missing slots
  - Login failures
  - Page load issues

---

#### 9. Automate Daily Execution
- Schedule your script using:
  - **Windows Task Scheduler**
  - **cron jobs** on Linux/Mac  
- Run the script at specific times when slots open.

---

💡 **Extra Challenges**:
- Add **email/WhatsApp notifications** after a successful booking.  
- Implement a **retry mechanism** if no slots are available.  
- Use **headless mode** to run the script without opening a browser window.  
- Extend functionality to book recurring sessions automatically.

