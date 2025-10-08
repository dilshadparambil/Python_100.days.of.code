# Day 67: Blog Capstone Project (Part 3 – RESTful Routing) 📝

In this stage of the Blog project, I integrated a **database** to store blog posts and implemented full **CRUD operations** (Create, Read, Update, Delete). I also added a **rich text editor** using **Flask-CKEditor** for better blog formatting and applied **RESTful routing** for a more structured app.

📄 [View My Code](my_code/d67.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 

---

## 🧠 Concepts Covered

- **Flask with SQLAlchemy ORM**: defining models and interacting with SQLite database.
- **RESTful Routing**: resource-based routes for blog posts (`/new-post`, `/edit-post/<id>`, `/delete/<id>`).
- **CRUD Operations**:
  - **Create** → Add new blog posts.
  - **Read** → Display all posts or individual post pages.
  - **Update** → Edit existing posts.
  - **Delete** → Remove posts from database.
- **WTForms with Flask-WTF** for form handling and validation.
- **Flask-CKEditor** integration for rich text blog content editing.
- **Jinja2 template inheritance** for modular templates (`header.html`, `footer.html`).
- **Bootstrap5** styling for consistent UI.

---

## 📝 Instructions

### 1. **Setup & Installation**

1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask server:
   ```bash
   python d67.py
   ```

3. Navigate to `http://127.0.0.1:5003/` in your browser.

### 2. Database Configuration

- **Database**: SQLite (posts.db)
- **Table**: BlogPost

**Fields**:

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| title | String | Title of the blog post |
| subtitle | String | Subtitle of the post |
| date | String | Date of creation/edit |
| body | Text | Blog content (HTML safe) |
| author | String | Author of the post |
| img_url | String | Background/cover image |

The database is auto-created if it doesn't exist.

### 3. RESTful Routes

**Home Page**
- `GET /` → Displays all blog posts.

**View Individual Post**
- `GET /post/<id>` → Shows a full blog post with title, content, and metadata.

**Create New Post**
- `GET /new-post` → Form page with CKEditor.
- `POST /new-post` → Submits and saves post to DB.

**Edit Post**
- `GET /edit-post/<id>` → Pre-fills form with existing content.
- `POST /edit-post/<id>` → Updates post in DB.

**Delete Post**
- `GET /delete/<id>` → Deletes the post by ID and redirects to homepage.

**Static Pages**
- `GET /about` → About page.
- `GET /contact` → Contact page.

### 4. WTForms Setup

Custom `AddPostForm` with fields:
- Title, Subtitle, Author, Image URL, Body (CKEditor).
- Includes validation (DataRequired, URL).
- Used for both new and edit post routes.

### 5. CKEditor Integration

Enables rich-text formatting in blog content.

**Configured via:**
```python
body = CKEditorField('Blog content', validators=[DataRequired()])
```

**Loaded in templates with:**
```jinja2
{{ ckeditor.load() }}
{{ ckeditor.config(name='body') }}
```

---

## 💡 Extra Challenges

- Add user authentication so only admins can add/edit/delete posts.
- Implement categories/tags for better blog organization.
- Add pagination for large numbers of blog posts.
- Enable file uploads for images instead of URLs.