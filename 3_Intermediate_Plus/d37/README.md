## Day 37: Habit Tracking Project  
A project that uses the Pixela API to track daily habits like workouts, coding practice, or water intake. Users can create graphs and update or delete entries programmatically.  

📄 [View Solution](solution.py) 📄 [View My Code](d37.py)  

### 🧠 Concepts Covered
- HTTP requests (`POST`, `PUT`, `DELETE`)  
- Using `datetime.strftime()` for date formatting  
- Advanced authentication with tokens and environment variables  
- Sending and parsing JSON data  
- RESTful API interaction  

### 📝 Instructions

1. **Set up Pixela account**  
   - Pixela is a service that lets you track habits visually on a graph.  
   - Go to [Pixela](https://pixe.la) and understand the API documentation.  

2. **Create a user account**  
   - Send a `POST` request to the Pixela endpoint:  
     ```
     https://pixe.la/v1/users
     ```  
   - Provide required JSON body with `username`, `token`, and agreement parameters.  
   - Example:  
     ```json
     {
       "token": "your_token_here",
       "username": "your_username",
       "agreeTermsOfService": "yes",
       "notMinor": "yes"
     }
     ```

3. **Create a graph**  
   - Use a `POST` request to create a graph under your account.  
   - Graph config includes `id`, `name`, `unit`, `type`, and `color`.  
   - Example endpoint:  
     ```
     https://pixe.la/v1/users/<username>/graphs
     ```

4. **Post a pixel (track a habit)**  
   - Use `POST` to add a daily record (called a pixel).  
   - Format the date using `datetime.now().strftime("%Y%m%d")`.  
   - Example JSON:  
     ```json
     {
       "date": "20250101",
       "quantity": "5"
     }
     ```

5. **Update a pixel**  
   - Use a `PUT` request if you want to modify the data for a specific date.  
   - Example endpoint:  
     ```
     https://pixe.la/v1/users/<username>/graphs/<graphID>/<date>
     ```

6. **Delete a pixel**  
   - Use a `DELETE` request to remove data for a given date.  

7. **Secure your authentication**  
   - Store the `token` in environment variables instead of hardcoding it in the script.  
   - Use `os.environ.get("PIXELA_TOKEN")` to fetch it.  

💡 **Extra Challenge**:  
- Automate the program to log habits daily.  
- Integrate with another service (e.g., send notifications after logging).  
- Track multiple habits using different graphs.  
