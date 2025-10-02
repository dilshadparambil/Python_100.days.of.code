## Day 64: Top 10 Movies Website 🎬  
A Flask + SQLite web app to keep track of your **Top 10 favourite movies**.  
It integrates with **The Movie Database (TMDB) API** to fetch movie details (title, description, release year, poster), and allows editing ratings, reviews, and managing a ranked list.  

📄 [View My Code](my_code/d64.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 

---

### 🧠 Concepts Covered
- **Flask with SQLAlchemy ORM** for database management  
- **SQLite3** database integration  
- **WTForms + Flask-WTF** for creating and validating forms  
- **Bootstrap-Flask** for styling forms and pages  
- **CRUD operations**:  
  - Create → Add new movies  
  - Read → View movies list  
  - Update → Edit movie ratings and reviews  
  - Delete → Remove a movie  
- **Dynamic ranking system** based on ratings  
- **Using APIs**: Fetch movie info from TMDB API  
- **Environment variables** (`TMDB_AUTH_TOKEN`) for secure API keys  
- **Jinja2 templates** for dynamic rendering with `for` loops and conditional logic  

---

### 📝 Instructions

1. **Install Required Packages**  
   Ensure dependencies are installed:  
   ```bash
   pip install flask flask-bootstrap flask-sqlalchemy flask-wtf requests
   ```

2. **Set Up Environment Variable for TMDB**  
   Get your **TMDB API Bearer Token** from [The Movie Database](https://www.themoviedb.org/documentation/api).  
   Export it in your terminal:  
   ```bash
   export TMDB_AUTH_TOKEN="your_api_token_here"
   ```

3. **Database Setup**  
   - A `Movies` table is created automatically with fields:  
     - `id` (Primary Key)  
     - `title`  
     - `year`  
     - `description`  
     - `rating`  
     - `ranking`  
     - `review`  
     - `img_url`  
   - `sqlite:///movie-list.db` is used for persistence.  

4. **Home Page (`/`)**  
   - Displays **Top 10 movies**, sorted by rating.  
   - Rankings (`1–10`) are dynamically updated each time the page loads.  
   - Each movie card shows:  
     - Poster  
     - Title + Year  
     - Rating + Review  
     - Description  
   - Buttons: **Update** and **Delete** for each entry.  

5. **Add a Movie (`/add`)**  
   - Displays a form (`AddForm`) to input a movie title.  
   - Calls TMDB Search API to fetch possible matches.  
   - Renders a `select.html` page with clickable movie options.  

6. **Select and Save Movie (`/get_movie`)**  
   - When a movie is selected, fetch its **detailed info** from TMDB API.  
   - Saves into the database with `title`, `year`, `description`, and `img_url`.  
   - Redirects to `/edit` to allow rating and review input.  

7. **Edit a Movie (`/edit`)**  
   - Form (`EditForm`) allows updating:  
     - Rating (out of 10)  
     - Review (short text)  
   - Updates the DB and returns to Home page.  

8. **Delete a Movie (`/delete`)**  
   - Removes selected movie from database.  
   - Redirects back to home page.  

9. **Run the Application**  
   ```bash
   python d64.py
   ```
   Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)  

---

💡 **Extra Challenge Ideas**  
- Allow uploading your own custom poster images.  
- Add authentication (only logged-in users can add/edit/delete).  
- Extend to **Top 100 movies** instead of 10.  
- Display **trailers** using TMDB video API.  
- Use star rating input UI instead of text fields.  
