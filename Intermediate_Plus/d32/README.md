## Day 32: Automated Birthday Wisher  
A program that checks if today matches anyone’s birthday from a CSV file and automatically sends them a personalized birthday email using a random letter template.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d32.py)  

### 🧠 Concepts Covered
- `smtplib` for sending emails programmatically  
- `datetime` for working with today’s date  
- Reading CSV data with Pandas  
- Dictionary comprehension for quick lookups  
- Using the `random` module to pick a template  
- String replacement with `.replace()`  

### 📝 Instructions

1. **Prepare the Birthday Data**  
   - Update `birthdays.csv` with your friends’ and family’s details:  
     ```csv
     name,email,year,month,day
     YourName,your_email@example.com,1995,8,27
     ```
   - Include at least one entry matching today’s date for testing.  

2. **Check for Today’s Birthdays**  
   - Use `datetime` to get today’s month and day:  
     ```python
     today = (today_month, today_day)
     ```  
   - Read the CSV with Pandas:  
     ```python
     data = pandas.read_csv("birthdays.csv")
     ```  
   - Create a lookup dictionary with dictionary comprehension:  
     ```python
     birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
     ```  
   - Check if today matches a key:  
     ```python
     if today in birthdays_dict:
         birthday_person = birthdays_dict[today]
     ```

3. **Pick a Random Letter Template**  
   - Store multiple letter templates in `letter_templates/` (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`).  
   - Use the `random` module to pick one:  
     ```python
     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
     with open(file_path) as letter_file:
         contents = letter_file.read()
         contents = contents.replace("[NAME]", birthday_person["name"])
     ```  

4. **Send the Birthday Email**  
   - Use `smtplib` to connect to an SMTP server (e.g., Gmail: `smtp.gmail.com`).  
   - Start TLS for security:  
     ```python
     connection.starttls()
     ```  
   - Login with your email and password (make sure “less secure apps” or app passwords are enabled).  
   - Send the message:  
     ```python
     connection.sendmail(
         from_addr=MY_EMAIL,
         to_addrs=birthday_person["email"],
         msg=f"Subject:Happy Birthday!\n\n{contents}"
     )
     ```

💡 **Extra Challenges**:
- Add more templates for variety.  
- Schedule the script to run daily with `cron` (Linux/Mac) or Task Scheduler (Windows).  
- Store multiple birthdays per day and send to all of them.  
- Use environment variables for secure storage of email credentials.  
