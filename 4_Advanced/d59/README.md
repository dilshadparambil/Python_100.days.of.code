## Day 59: Blog Capstone Project (Part 2 - Adding Styling)  
Enhancement of the Flask Blog project by integrating **Bootstrap** and custom styling to improve layout, typography, and user experience.

📄 [View My Code](my_code/d59.py)  📄 [View Solution](solution/solution.py) 
📄 [View My Html](my_code/templates/index.html)  📄 [View Solution Html](solution/templates/index.html) 

### 🧠 Concepts Covered
- Flask with Jinja templating for dynamic HTML rendering  
- Integrating **Bootstrap** for responsive design  
- Structuring HTML with reusable templates (`header.html`, `footer.html`)  
- Adding static files (CSS, images, JS) in Flask apps  
- Styling blog posts with Bootstrap components (`container`, `row`, `col`, `masthead`, etc.)  
- Customizing page headers and backgrounds with CSS  
- Using Jinja loops and variables to dynamically generate styled content  

### 📝 Instructions
1. **Set up the project structure**  
   - Keep HTML templates in the `templates/` folder.  
   - Place static assets (CSS, JS, images) in the `static/` folder.  
   - Split your base layout into `header.html` and `footer.html` to reuse across all pages.  

2. **Integrate Bootstrap**  
   - Include Bootstrap via CDN in `header.html`.  
   - Use Bootstrap grid system (`container`, `row`, `col-md-*`) to make the blog responsive.  

3. **Style the Homepage**  
   - Add a masthead banner with a background image using inline CSS:  
     ```html
     <header class="masthead" style="background-image: url('static/assets/img/home-bg.jpg')">
     ```
   - Display blog title and subtitle in the banner.  

4. **Render Blog Posts Dynamically**  
   - Use Jinja to loop through `blogs` and render post previews:  
     ```html
     {% for blog in blogs: %}
       <div class="post-preview">
           <a href="{{url_for('post',blog_id=blog.id)}}">
               <h2 class="post-title">{{ blog.title }}</h2>
               <h3 class="post-subtitle">{{ blog.subtitle }}</h3>
           </a>
           <p class="post-meta">Posted by <a href="#!">{{ blog.author }}</a> on {{ blog.date }}</p>
       </div>
       <hr class="my-4" />
     {% endfor %}
     ```

5. **Add Navigation and Footer**  
   - Include a navigation bar in `header.html`.  
   - Add a styled footer in `footer.html` with Bootstrap classes.  

6. **Style Individual Blog Pages**  
   - For each blog post (`post.html`), use Bootstrap cards or containers to make content readable.  
   - Apply margins, padding, and typography styles for better readability.  

7. **Extra Enhancements**  
   - Add a **"Read More"** button styled with Bootstrap.  
   - Use Bootstrap utilities for spacing, text alignment, and colors.  
   - Create a consistent color theme with a custom CSS file inside `static/css/`.  

💡 **Extra Challenge**:  
- Implement pagination with Bootstrap buttons.  
- Add responsive navigation that collapses into a hamburger menu on smaller screens.  
- Experiment with different Bootstrap themes or customize your own.  
