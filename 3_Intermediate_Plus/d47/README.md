## Day 47: Automated Amazon Price Tracker  
A Python script that monitors the price of a specific Amazon product and sends an email alert when the price drops below a specified threshold.  

📄 [View Solution](solution.py) 📄 [View My Code](d47.py)  

### 🧠 Concepts Covered
- Web scraping with `requests` and `BeautifulSoup`  
- Parsing and extracting product details from HTML  
- Automating price monitoring  
- Sending emails with `smtplib`  
- Environment variables for secure credentials  
- String manipulation and data cleaning  
- Conditional logic for alert triggers  

### 📝 Instructions
1. **Choose a Product to Track**  
   - Go to [Amazon](https://www.amazon.com/) and find the product you want to monitor.  
   - Copy the product URL for use in your script.  
   - Note: Make sure the product is available in your region and doesn’t require login to view.

2. **Install Required Libraries**  
   Install the libraries for web scraping and email notifications:  
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Scrape Product Details**  
   - Use `requests.get()` to fetch the Amazon product page.  
   - Add headers with `User-Agent` and `Accept-Language` to mimic a browser.  
   - Parse the HTML with `BeautifulSoup`.  
   - Extract:  
     - **Product Title** (for reference in the email)  
     - **Price** (convert it into a float for comparison).

4. **Set a Price Threshold**  
   - Define a variable for your target price (e.g., `$100`).  
   - If the product’s current price is less than or equal to this threshold, trigger the alert.

5. **Send Email Notification**  
   - Use `smtplib.SMTP()` with `smtp.gmail.com`, `smtp.live.com`, or `smtp.mail.yahoo.com`.  
   - Enable `.starttls()` for encryption.  
   - Login with your email and app password (use environment variables to store credentials).  
   - Send an email to yourself containing:  
     - Product name  
     - Current price  
     - Product link

6. **Schedule the Script**  
   - Run the script manually or automate it with:  
     - **cron job** (Linux/macOS)  
     - **Task Scheduler** (Windows)

💡 **Extra Challenge**:
- Log price history in a `.csv` or `.json` file.  
- Track multiple products at once.  
- Send notifications via WhatsApp using Twilio API.  
- Deploy to a cloud service (AWS Lambda, Heroku, etc.) for automation.  
