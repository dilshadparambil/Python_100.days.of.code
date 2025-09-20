## Day 53: Zillow Data Entry Bot  
A bot that scrapes property rental data from Zillow and automatically fills it into a Google Form for data collection.  

📄 [View Solution](solution.py) 📄 [View My Code](d53.py)  

---

### 🧠 Concepts Covered
- **Web scraping** with BeautifulSoup and Requests  
- **Selenium WebDriver** for form automation  
- **CSS selectors & XPath** for locating dynamic elements  
- **Data extraction**: property links, prices, and addresses  
- **Google Form automation** with Selenium  
- **Loops** for processing multiple listings  
- **Error handling** for dynamic content and pop-ups  
- **Environment variables** for managing form URLs and sensitive configs  

---

### 📝 Instructions

#### 1. Install Dependencies
```bash
pip install selenium
pip install beautifulsoup4
pip install requests
pip install python-dotenv
```
Ensure ChromeDriver (or your browser’s WebDriver) is installed and in PATH.  

---

#### 2. Set Up Environment Variables
Create a `.env` file:
```env
FORM_URL=https://docs.google.com/forms/d/e/your-form-id/viewform
ZILLOW_URL=https://www.zillow.com/homes/for_rent/
```

---

#### 3. Scrape Zillow Data
- Use `requests` to fetch Zillow HTML.  
- Parse with BeautifulSoup:
```python
soup = BeautifulSoup(response.text, "html.parser")
prices = soup.select(".list-card-price")
addresses = soup.select(".list-card-addr")
links = soup.select(".list-card-top a")
```
- Store extracted details in lists.  

---

#### 4. Launch Google Form with Selenium
- Open the form:
```python
driver.get(FORM_URL)
```

---

#### 5. Automate Form Filling
- Locate fields using XPath or CSS selectors:
```python
address_input = driver.find_element(By.XPATH, "//input[@type='text'][1]")
price_input = driver.find_element(By.XPATH, "//input[@type='text'][2]")
link_input = driver.find_element(By.XPATH, "//input[@type='text'][3]")
```
- Send data:
```python
address_input.send_keys(address)
price_input.send_keys(price)
link_input.send_keys(link)
```

---

#### 6. Submit Form
- Locate and click submit button:
```python
submit_btn = driver.find_element(By.XPATH, "//span[text()='Submit']")
submit_btn.click()
```

---

#### 7. Loop Through All Listings
- Use a `for` loop to repeat steps for all scraped properties.  
- After submission, click **“Submit another response”** to reset the form.  

---

#### 8. Error Handling
- Handle missing prices or links with `try/except`.  
- Use `time.sleep()` or `WebDriverWait` to manage delays.  

---

💡 **Extra Challenges**:
- Save scraped data to **CSV/Excel** in addition to Google Forms.  
- Use **headless browser mode** for faster automation.  
- Schedule the script to run daily and update form automatically.  
