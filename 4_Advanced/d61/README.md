## Day 61: Secrets Website  
A small **Flask web app** that demonstrates secure form handling with **Flask-WTF**, styled with **Bootstrap-Flask**. Users can attempt to log in, and access is granted only if they enter the correct credentials. The project also introduces **Jinja2 template inheritance** for reusing layouts.

📄 [View My Code](my_code/d61.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 

---

### 🧠 Concepts Covered
- **Flask-WTF** for form handling and validation  
- **WTForms validators** (`DataRequired`, `Email`, `Length`)  
- **Bootstrap-Flask** for styling and integrating forms  
- **Template inheritance** with Jinja2 (`{% extends %}`, `{% block %}`)  
- **Secure session handling** with Flask’s `secret_key`  
- Returning different templates depending on login success or failure  

---

### 📝 Instructions

1. **Install Required Packages**  
   Make sure you have all dependencies installed via `requirements.txt`:  
   ```bash
   # On Windows
   python -m pip install -r requirements.txt  

   # On macOS/Linux
   pip3 install -r requirements.txt  
   ```

2. **Set Up Flask App**  
   - Create a Flask project with `main.py`.  
   - Initialize Flask, set a `secret_key`, and configure **Bootstrap5**.  

3. **Create a Login Form using Flask-WTF**  
   Define a custom form class with validators:  
   ```python
   class MyForm(FlaskForm):
       email = StringField(label='Email', validators=[DataRequired(), Email()])
       password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
       submit = SubmitField(label='Login')
   ```

4. **Build Routes**  
   - `/` → Home page with a welcome message and link to login.  
   - `/login` → Shows the login form, validates credentials, and displays either `success.html` or `denied.html`.  

5. **Use Template Inheritance with Jinja2**  
   - Create a `base.html` with shared blocks for **title**, **styling**, **body**, and **scripts**.  
   - Extend `base.html` in all other templates (`index.html`, `login.html`, `success.html`, `denied.html`).  

6. **Render the Login Form with Bootstrap-Flask**  
   Use the built-in `render_form` macro to automatically render the form with Bootstrap styles:  
   ```html
   {% from 'bootstrap5/form.html' import render_form %}
   {{ render_form(form, novalidate=False) }}
   ```

7. **Handle Login Logic**  
   - If the form validates and email/password match `"admin@email.com"` and `"12345678"`, show `success.html`.  
   - Otherwise, show `denied.html`.  

8. **Add GIPHY Embeds for Feedback**  
   - `success.html` → Shows a celebratory GIF.  
   - `denied.html` → Shows an “Access Denied” GIF.  

---

💡 **Extra Challenge**:
- Add user registration with hashed passwords.  
- Store users in a database (e.g., SQLite with SQLAlchemy).  
- Extend the form with a "Remember Me" checkbox.  
- Use Flask-WTF’s CSRF protection features.  
