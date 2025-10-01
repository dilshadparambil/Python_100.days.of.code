## Day 63: Virtual Bookshelf 📚  
A Flask + SQLite3 web application to store, update, and delete books.  
This project demonstrates **CRUD (Create, Read, Update, Delete)** operations with SQLAlchemy ORM and a simple HTML interface.  

📄 [View My Code](my_code/d63.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 

---

### 🧠 Concepts Covered
- **SQLite3 database** setup and integration with Flask  
- **SQLAlchemy ORM** for object-relational mapping  
- **DeclarativeBase** and `mapped_column` for defining models  
- **CRUD operations**:  
  - Create → Add new book entries  
  - Read → Display all books  
  - Update → Edit book rating  
  - Delete → Remove a book from the database  
- **Flask routes** for handling user actions (`/add`, `/edit`, `/delete`)  
- Using **HTML forms** to capture user input  
- **Redirecting and URL parameters** with Flask (`url_for`, `request.args`)  

---

### 📝 Instructions

1. **Install Required Packages**  
   Make sure Flask and SQLAlchemy are installed:  
   ```bash
   # On Windows
   python -m pip install -r requirements.txt  

   # On macOS/Linux
   pip3 install -r requirements.txt  
   ```

2. **Set Up Database**  
   - Configure Flask to use SQLite database:  
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///all-books.db'
     ```
   - Define `Books` model with fields:  
     - `id` (Primary Key)  
     - `title` (String, unique, required)  
     - `author` (String, required)  
     - `rating` (Float, required)  
   - Create the database with:
     ```python
     with app.app_context():
         db.create_all()
     ```

3. **Display All Books (Home Page)**  
   - Route `/` queries all books using:
     ```python
     result = db.session.execute(db.select(Books))
     all_books = result.scalars().all()
     ```
   - Pass results to `index.html` and render them in a list.  
   - Show "Library is empty" if no books exist.  

4. **Add a New Book**  
   - Route `/add` supports `GET` (show form) and `POST` (submit new book).  
   - In `add.html`, create a form with fields for name, author, and rating.  
   - On submission:
     ```python
     add_data = Books(title=request.form['book_name'], author=request.form['book_author'], rating=request.form['book_rating'])
     db.session.add(add_data)
     db.session.commit()
     ```
   - Redirect back to home page.  

5. **Edit Book Rating**  
   - Route `/edit` retrieves book by `id` from query parameters.  
   - If `POST`, update the rating:
     ```python
     book_data.rating = float(request.form['new_rating'])
     db.session.commit()
     ```
   - Render `edit.html` with current book info and a field to enter new rating.  

6. **Delete a Book**  
   - Route `/delete` retrieves book by `id`.  
   - Delete from database:
     ```python
     db.session.delete(book_data)
     db.session.commit()
     ```
   - Redirect back to home page.  

7. **Run the Application**  
   Start the Flask development server:  
   ```bash
   python d63.py
   ```
   Visit `http://127.0.0.1:5000` in your browser.  

---

💡 **Extra Challenge**  
- Add new fields like `genre` or `year published`.  
- Use Flask-WTF forms for validation instead of raw HTML forms.  
- Integrate Bootstrap for styling.  
- Add sorting functionality (e.g., highest-rated first).  
- Implement user authentication to manage books.  
