## Day 57: Blog Capstone Project (Part 1 – Templating)  
A simple blog application built with Flask and Jinja templating. This project fetches blog posts from an API, renders them dynamically in templates, and allows navigation to individual post pages.  

📄 [View My Code](my_code/d57.py) 📄 [Html files](my_code/templates/index.html) 📄 [View Solution](solution/solution.py) 📄 [Solution Html](solution/templates/index.html)  

### 🧠 Concepts Covered
- Flask framework basics (`Flask`, `render_template`)  
- Class creation for structured data (`Post` class)  
- Using **requests** to fetch API data  
- Jinja2 templating (`{{ }}`, `{% %}`)  
- URL routing and dynamic paths (`/post/<int:index>`)  
- Passing objects to templates  
- Template iteration with `{% for %}` loops  
- Linking routes with `url_for()`  

### 📝 Instructions  

1. **Set up the Post Class**  
   - Create a `Post` class in `posts.py` with attributes:  
     - `id` → unique post identifier  
     - `title` → post title  
     - `subtitle` → short description  
     - `body` → full post content  

2. **Fetch Blog Data**  
   - Use the `requests` library to fetch JSON data from:  
     ```
     https://api.npoint.io/5abcca6f4e39b4955965
     ```
   - Convert each post dictionary into a `Post` object.  
   - Append all objects to a list `post_objects`.  

3. **Set up Flask App (`d57.py`)**  
   - Initialize a Flask app with `app = Flask(__name__)`.  
   - Create a route `/` to display all posts.  
   - Create a route `/post/<int:index>` for individual post details.  

4. **Create Templates**  
   - **index.html**  
     - Loop through `all_posts`.  
     - Display `title` and `subtitle` for each post.  
     - Add a `Read` link that points to the full post page using:  
       ```jinja
       <a href="{{ url_for('show_post', index=post.id) }}">Read</a>
       ```  

   - **post.html**  
     - Display the selected post’s `title`, `subtitle`, and `body`.  

5. **Apply Styling**  
   - Link Google Fonts (`Raleway`) for better typography.  
   - Connect a CSS file from `../static/css/styles.css`.  
   - Use `.wrapper`, `.top`, and `.card` classes for layout.  

6. **Run the App**  
   - Run the app with:  
     ```bash
     python d57.py
     ```  
   - Open `http://127.0.0.1:5000/` in a browser.  
   - Click on a blog post link to navigate to the full article page.  

💡 **Extra Challenge**:  
- Add a homepage banner with an introduction.  
- Include author names and dates in posts.  
- Add navigation links (Home, About, Contact).  
- Improve styles with CSS grid/flexbox for responsive design.  
