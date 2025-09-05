## Day 38: Workout Tracking Project  
A project that uses **APIs** to track workouts, calculate calories burned, and store the data in a spreadsheet via Sheety.  

📄 [View Solution](solution.py) 📄 [View My Code](d38.py)  

### 🧠 Concepts Covered
- **HTTP Requests** (`POST`) for API communication  
- **Working with multiple APIs** (Nutritionix API for workout analysis, Sheety API for data storage)  
- **JSON data parsing and creation**  
- **Environment variables** for secure storage of API keys and tokens  
- **Datetime module** for timestamps (`datetime.now()`)  
- **Automating workflows** using Python scripts and APIs  

---

### 📝 Instructions

1. **Set up Nutritionix API**  
   - Create a free Nutritionix account.  
   - Retrieve your **App ID** and **API Key**.  
   - Use the Nutritionix Natural Language Exercise endpoint to analyze workouts based on a user’s text input.  
   - Example: Input `"Ran 3 miles"` → API returns calories, duration, and estimated data.

2. **Take User Input**  
   - Prompt the user to enter their workout (e.g., `"Tell me what exercise you did today:"`).  
   - Send this input to the Nutritionix API for processing.

3. **Parse API Response**  
   - Extract relevant data such as:  
     - Exercise name  
     - Duration (in minutes)  
     - Calories burned  

4. **Store Data Using Sheety API**  
   - Set up a free Sheety project linked to a Google Sheet.  
   - Format your sheet to have columns like **Date**, **Time**, **Exercise**, **Duration**, and **Calories**.  
   - Use a `POST` request to send parsed data to Sheety, automatically logging workouts to the sheet.  

5. **Add Timestamp**  
   - Use Python’s `datetime` module to capture the current date and time dynamically.  
   - Example:
     ```python
     from datetime import datetime
     today = datetime.now()
     date = today.strftime("%Y-%m-%d")
     time = today.strftime("%H:%M:%S")
     ```

6. **Secure API Keys**  
   - Store sensitive information (Nutritionix ID, API Key, Sheety Token) in environment variables.  
   - Use `os.environ.get("API_KEY")` to retrieve them in your script.  

7. **Test and Automate**  
   - Run your program to log workouts in real-time.  
   - Optionally, schedule this script to run automatically each day.  

---

💡 **Extra Challenge**:
- Add user authentication to secure your app.  
- Track different metrics like heart rate or distance if your API supports it.  
- Integrate with additional services like Notion or Airtable instead of Google Sheets.  
