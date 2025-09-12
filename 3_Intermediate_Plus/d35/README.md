## Day 35: Rain Alert App  
A Python app that checks the weather forecast using an API and sends a WhatsApp alert if it’s going to rain.  

📄 [View Solution](solution.py) 📄 [View My Code](d35.py)  

### 🧠 Concepts Covered
- Working with APIs (requests, parameters, JSON responses)  
- API keys and authentication  
- Environment variables for storing sensitive data securely  
- Sending WhatsApp messages using Twilio API  
- Conditional logic for triggering alerts  

### 📝 Instructions
1. **Get Weather API Access**  
   - Sign up on [OpenWeatherMap](https://openweathermap.org/api) (or similar service).  
   - Generate an API key.  
   - Save the key in environment variables for security.  

2. **Make an API Call**  
   - Use the `requests` library to call the weather API.  
   - Pass parameters such as `lat`, `lon`, and `appid` (API key).  
   - Set units to `metric` or `imperial` depending on preference.  
   - Parse the JSON response to extract hourly/daily forecast data.  

3. **Check for Rain**  
   - Loop through the forecast data (e.g., next 12 hours).  
   - Look for weather conditions with `"rain"` in the description or a weather code indicating rain.  

4. **Set up Twilio for WhatsApp Messaging**  
   - Create a Twilio account and verify your WhatsApp number.  
   - Get `account_sid`, `auth_token`, and a Twilio WhatsApp-enabled number.  
   - Store them as environment variables for security.  

5. **Send a WhatsApp Alert**  
   - If rain is detected, use the Twilio API to send a message like:  
     `"It's going to rain today. Remember to bring an umbrella ☔"`  
   - Example Twilio send code:  
     ```python
     from twilio.rest import Client

     client = Client(account_sid, auth_token)
     message = client.messages.create(
         body="It's going to rain today. Bring an umbrella ☔",
         from_="whatsapp:+14155238886",  # Twilio sandbox number
         to="whatsapp:+91xxxxxxxxxx"     # Your verified number
     )
     print(message.sid)
     ```

6. **Run the App**  
   - Execute the script.  
   - If rain is predicted in the next few hours, you’ll receive a WhatsApp notification.  

💡 **Extra Challenge**:  
- Extend the app to handle multiple cities.  
- Add SMS/email alerts as an alternative.  
- Schedule the app with a task scheduler (e.g., cron job or Windows Task Scheduler) to run daily.  
