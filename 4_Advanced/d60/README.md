## Day 60: Blog Capstone Project (Part 2a – Contact Form with POST Request)  
In this stage of the Blog project, a **contact form** is added to allow visitors to send messages directly via email. The form is built using **HTML forms** and processed using Flask’s `POST` request handling. Emails are sent securely using **SMTP** and environment variables for credentials.

📄 [View My Code](my_code/d60.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 
---

### 🧠 Concepts Covered
- Flask routes with **GET** and **POST** methods  
- Handling form submissions using `request.form`  
- Using **smtplib** to send emails programmatically  
- Securing email credentials with **environment variables**  
- Using **HTML forms** (`<form>`, `<input>`, `<textarea>`) to capture user input  
- Dynamic rendering of success/failure messages in templates  
- Integrating contact functionality into an existing blog  

---

### 📝 Instructions

1. **Set Up Environment Variables**  
   - Create an environment variable for your email app password:  
     ```bash
     export EMAIL_APP_PASS="your_app_password"
     ```
   - Store your main email address in the code (or also in `.env` for better security).  

2. **Create a Contact Form in HTML (`contact.html`)**  
   Example form structure:  
   ```html
   <form method="POST" action="{{ url_for('contact') }}">
       <input type="text" name="name" placeholder="Your Name" required><br>
       <input type="email" name="email" placeholder="Your Email" required><br>
       <input type="tel" name="phone" placeholder="Your Phone"><br>
       <textarea name="message" placeholder="Your Message" required></textarea><br>
       <button type="submit">Send</button>
   </form>
   ```

3. **Update Flask Route to Handle POST Request**  
   In `main.py`, modify `/contact` route:  
   ```python
   @app.route('/contact', methods=['GET','POST'])
   def contact():
       if request.method == 'POST':
           name = request.form['name']
           email = request.form['email']
           phone = request.form['phone']
           message = request.form['message']

           with smtplib.SMTP('smtp.gmail.com') as connection:
               connection.starttls()
               connection.login(user=EMAIL, password=EMAIL_APP_PASS)
               connection.sendmail(
                   from_addr=EMAIL,
                   to_addrs="your_email_here@gmail.com",
                   msg=f"Subject: New Contact Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
               )
           return render_template("contact.html", title="Successfully sent message")
       return render_template("contact.html", title="Contact Me")
   ```

4. **Add Navigation to Contact Page**  
   Update `header.html` to include a Contact link:  
   ```html
   <a class="nav-link" href="{{ url_for('contact') }}">Contact</a>
   ```

5. **Test Email Functionality**  
   - Start your Flask server and navigate to `/contact`.  
   - Fill out the form and verify that an email is sent to your inbox.  

6. **Error Handling (Optional)**  
   - Wrap email sending logic in a `try/except` block to handle errors (like invalid credentials or network issues).  
   - Show an error message in the template if sending fails.  

---

💡 **Extra Challenge**:
- Add Bootstrap styling to the form (labels, input groups, responsive layout).  
- Use Flask-WTF for form validation.  
- Store messages in a database in addition to sending them via email.  
