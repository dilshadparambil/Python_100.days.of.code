## Day 33: ISS Tracker  
A program that checks the position of the International Space Station (ISS) and sends a notification if it is overhead during nighttime.  

📄 [View Solution](solution.py) 📄 [View My Code](d33.py)  

### 🧠 Concepts Covered
- Making API requests with the `requests` library  
- Handling JSON responses from APIs  
- Using query parameters in API calls  
- Working with latitude/longitude data  
- Using `datetime` to check sunrise and sunset times  
- Conditional logic to determine visibility  

### 📝 Instructions

1. **Fetch the Current ISS Position**  
   - Use the Open Notify API: `http://api.open-notify.org/iss-now.json`  
   - Send a request with `requests.get()` and parse the JSON response:  
     ```python
     response = requests.get("http://api.open-notify.org/iss-now.json")
     data = response.json()
     iss_latitude = float(data["iss_position"]["latitude"])
     iss_longitude = float(data["iss_position"]["longitude"])
     ```

2. **Check Proximity to Your Location**  
   - Define your latitude and longitude (e.g., `MY_LAT = 28.7041`, `MY_LONG = 77.1025`).  
   - The ISS is considered “close” if it is within ±5 degrees of both latitude and longitude.  

3. **Get Sunrise and Sunset Times**  
   - Use the Sunrise-Sunset API: `https://api.sunrise-sunset.org/json`  
   - Pass your location and format as parameters:  
     ```python
     parameters = {
         "lat": MY_LAT,
         "lng": MY_LONG,
         "formatted": 0
     }
     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
     data = response.json()
     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
     ```  

4. **Check if it’s Nighttime**  
   - Get the current hour with `datetime.now().hour`.  
   - If the current time is after sunset or before sunrise, it’s dark enough to see the ISS.  

5. **Combine the Conditions**  
   - If the ISS is nearby **and** it’s nighttime, send yourself a notification (e.g., print message or send email).  

6. **Automate the Check**  
   - Wrap the logic in a loop that runs every 60 seconds using `time.sleep(60)`.  
   - Continue checking until conditions are met.  

💡 **Extra Challenges**:
- Send an actual email notification with `smtplib`.  
- Use a push notification service (e.g., Twilio or Pushover).  
- Extend the program to log ISS sightings to a file.  
