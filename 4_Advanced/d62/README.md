## Day 62: Coffee and Wifi ☕️💻  
A Flask web application where users can add and view cafes along with details like opening hours, coffee quality, Wi-Fi strength, and power availability. The app stores cafe data in a CSV file and displays it in a Bootstrap-styled table.  

📄 [View My Code](my_code/d62.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 

---

### 🧠 Concepts Covered
- **Flask-WTF forms** with `StringField`, `SelectField`, and validators (`DataRequired`, `URL`)  
- **Bootstrap-Flask** for styling forms and pages  
- **Template inheritance** in Jinja2 (`base.html` as layout)  
- **Form validation** and writing to CSV files  
- **Reading CSV files** and dynamically rendering rows in HTML tables  
- **Using SelectField choices** with emoji ratings (☕️, 💪, 🔌)  
- Linking and rendering Google Maps URLs dynamically  

---

### 📝 Instructions  

1. **Install Required Packages**  
   Make sure to install the necessary libraries using `requirements.txt`:  
   ```bash
   # On Windows
   python -m pip install -r requirements.txt  

   # On macOS/Linux
   pip3 install -r requirements.txt  
   ```

2. **Set Up Flask Application**  
   - Create a Flask app in `d62.py`.  
   - Configure `SECRET_KEY` for Flask-WTF forms.  
   - Initialize `Bootstrap5(app)` for styling.  

3. **Create a Cafe Form**  
   Define a `CafeForm` class with fields:  
   - `cafe` → Cafe name (`StringField`)  
   - `location_url` → Google Maps link (`StringField` with `URL` validator)  
   - `opening_time`, `closing_time` → Opening/closing hours (`StringField`)  
   - `coffee_rating` → Select 1–5 ☕️ emojis  
   - `wifi_rating` → Select ✘ or 💪 (1–5 strength)  
   - `power_rating` → Select ✘ or 🔌 (1–5 outlets)  
   - `submit` → Submit button  

   Example:  
   ```python
   coffee_rating = SelectField('coffee rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
   ```

4. **Create Routes**  
   - `/` → Home page with project intro.  
   - `/add` → Displays the cafe form.  
     - On `POST`, validate the form and append cafe data to `cafe-data.csv`.  
   - `/cafes` → Reads `cafe-data.csv` and renders data in a Bootstrap-styled table.  

5. **Use Template Inheritance**  
   - `base.html` contains Bootstrap and global structure.  
   - Extend `base.html` in all templates (`index.html`, `add.html`, `cafes.html`).  

6. **Render Forms with Bootstrap-Flask**  
   In `add.html`:  
   ```html
   {% from 'bootstrap5/form.html' import render_form %}
   {{ render_form(form, novalidate=True) }}
   ```

7. **Render Cafe Data in Tables**  
   In `cafes.html`, loop through CSV rows:  
   - If an item starts with `http`, render it as a clickable Maps link.  
   - Otherwise, render the text normally.  

   Example:  
   ```html
   {% for rows in cafes: %}
     <tr>
       {% for item in rows: %}
         {% if item.startswith('http'): %}
           <td><a href="{{item}}">Maps Link</a></td>
         {% else: %}
           <td>{{item}}</td>
         {% endif %}
       {% endfor %}
     </tr>
   {% endfor %}
   ```

8. **Run the Application**  
   ```bash
   python d62.py
   ```
   Visit `http://127.0.0.1:5000` in your browser.  

---

💡 **Extra Challenge**  
- Add form fields for seating capacity and noise level.  
- Store data in a database (SQLite with SQLAlchemy) instead of CSV.  
- Implement sorting and filtering (e.g., show best Wi-Fi cafes first).  
- Add the ability to delete or edit cafes.  
