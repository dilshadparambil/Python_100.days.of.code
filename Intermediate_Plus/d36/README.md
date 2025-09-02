## Day 36: Stock News Monitoring Project  
An app that monitors stock price changes and sends relevant news updates if the stock moves significantly.  

📄 [View Solution](solution.py) 📄 [View My Code](d36.py)  

### 🧠 Concepts Covered
- Working with APIs (Alpha Vantage for stock data, News API for headlines)  
- API keys and authentication  
- Using environment variables to protect sensitive keys  
- JSON parsing from API responses  
- Conditional logic to trigger actions  
- Sending notifications via Twilio (SMS/WhatsApp)  

### 📝 Instructions
1. **Get API Access**  
   - Sign up for [Alpha Vantage](https://www.alphavantage.co/) to get stock market data.  
   - Sign up for [News API](https://newsapi.org/) to fetch news articles.  
   - Save both API keys in environment variables for security.  

2. **Fetch Stock Price Data**  
   - Use the `requests` library to call the Alpha Vantage API.  
   - Request daily stock data (`TIME_SERIES_DAILY`).  
   - Parse the JSON response and extract the closing prices for the last two days.  

3. **Calculate Percentage Change**  
   - Compare yesterday’s closing price with the day before.  
   - Calculate the percentage difference:  
     ```python
     change_percent = ((yesterday_close - day_before_close) / day_before_close) * 100
     ```  

4. **Check if Alert is Needed**  
   - Define a threshold (e.g., 5%).  
   - If the absolute percentage change is greater than or equal to the threshold, proceed to fetch news.  

5. **Fetch News Articles**  
   - Use the News API to search for the company’s name.  
   - Retrieve the top 3 articles related to the stock/company.  
   - Extract the title and description of each article.  

6. **Format the Alert Message**  
   - Create a formatted message combining stock movement and news articles, e.g.:  
     ```
     TSLA: 🔺5%  
     Headline: Tesla launches new model  
     Brief: Tesla announces a new model expected to increase sales.
     ```  

7. **Send Notification via Twilio**  
   - Use Twilio’s API to send the message via SMS or WhatsApp.  
   - Ensure credentials (`account_sid`, `auth_token`) are stored in environment variables.  

8. **Run the App**  
   - Execute the script.  
   - If the stock price change exceeds the threshold, you’ll receive news updates via SMS/WhatsApp.  

💡 **Extra Challenge**:  
- Allow multiple stock symbols to be monitored.  
- Save stock movement and news logs to a file or database.  
- Automate execution with a scheduler (cron job or Task Scheduler).  
