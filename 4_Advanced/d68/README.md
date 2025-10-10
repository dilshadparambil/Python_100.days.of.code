# Day 68: Flask Authentication 🔐

In this project, I built a **Flask web app** with **user authentication**.  
It uses **hashed and salted passwords** for security, **Flask-Login** for session management, and **Flask flash messages** to provide feedback to users during login/registration.

📄 [View My Code](my_code/d68.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 

---

## 🧠 Concepts Covered

- **Authentication** in Flask applications.
- **Hashing and salting** passwords with `werkzeug.security`.
- **Flask-Login** for managing user sessions.
- **Flask flash messages** for user feedback.
- **SQLAlchemy ORM** for database models and queries.
- **Login-required decorators** to restrict access to specific routes.
- Serving **protected files** only to logged-in users.

---

## 📝 Instructions

### 1. Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python d68.py
   ```

3. Navigate to `http://127.0.0.1:5000/`.

### 2. Database Configuration

- **Database**: SQLite (users.db)
- **Table**: User

**Fields**:

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| email | String | User's email (unique) |
| password | String | Hashed & salted password |
| name | String | User's display name |

### 3. Authentication Flow

**Register**
- `GET /register` → Displays the registration form.
- `POST /register` → Creates a new user with hashed password.
  - If email already exists → Shows flash message and redirects to login.
  - Automatically logs in the new user.

**Login**
- `GET /login` → Displays login form.
- `POST /login` → Authenticates user:
  - If email doesn't exist → Flash message.
  - If password incorrect → Flash message.
  - If valid → Logs in the user with Flask-Login.

**Secrets (Protected Page)**
- `GET /secrets` → Only accessible if logged in (`@login_required`).
- Displays a personalized welcome message.

**Logout**
- `GET /logout` → Logs out the user and redirects to home.

**File Download (Protected Resource)**
- `GET /download` → Only logged-in users can access/download `cheat_sheet.pdf`.

### 4. Password Security

Passwords are never stored in plain text.

**During registration:**
```python
hashed_password = generate_password_hash(
    request.form['password'],
    method='pbkdf2:sha256',
    salt_length=8
)
```

**During login:**
```python
check_password_hash(user.password, entered_password)
```

### 5. Flash Messages

Used for feedback (invalid email, wrong password, etc.).

**Displayed in templates with:**
```jinja2
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      <p>{{ message }}</p>
    {% endfor %}
  {% endif %}
{% endwith %}
```

---

## 💡 Extra Challenges

- Add email confirmation before account activation.
- Implement remember me functionality in Flask-Login.
- Allow users to update their profile info and password.
- Add role-based access (admin vs. regular users).