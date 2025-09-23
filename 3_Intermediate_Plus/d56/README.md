## Day 56: Name Card Website  
A simple portfolio-style personal webpage that displays your name, profile picture, profession, and social links. Built with HTML, CSS, and Flask integration.  

📄 [View My Code](d56.py) 📄 [View Html](templates/index.html)  

### 🧠 Concepts Covered
- **HTML structure**: semantic tags like `<header>`, `<footer>`, `<section>`  
- **CSS styling**: external stylesheet for layout, colors, and responsiveness  
- **Flask basics**: serving static files and HTML templates  
- **Static assets**: linking stylesheets and images from a `/static` folder  
- **Responsive design**: viewport meta tag and conditional CSS for IE browsers  
- **Social links with icons**: embedding LinkedIn, GitHub, and WhatsApp links  

### 📝 Instructions
1. **Set up Flask App**  
   - Create a Flask project with a basic route to serve the `index.html`.  
   - Configure the `/static` folder to store CSS, JS, and image files.  

2. **Create HTML Structure**  
   - Add a `<head>` section with title, meta viewport, and CSS links.  
   - Build a `<body>` containing a wrapper `<div>` with sections:  
     - **Header** → profile picture (`avatar.jpeg`), name, and profession.  
     - **Social Links** → list of links to LinkedIn, GitHub, and WhatsApp.  
     - **Footer** → copyright.

3. **Add CSS Styling**  
   - Link `main.css` (and fallback styles for IE if needed).  
   - Define styles for wrapper, avatar image, header text, and social icons.  
   - Add a `noscript.css` fallback for users with JavaScript disabled.  

4. **Embed Profile Content**  
   - Replace placeholder text with your name, title (e.g., *Python Developer*), and avatar image in `static/images/avatar.jpeg`.  
   - Add links for your real social profiles in the `<ul class="icons">`.  

5. **Enhance with JavaScript**  
   - Add a small script to handle page load transitions and browser compatibility.  

6. **Run Flask App**  
   - Start the Flask development server and open `http://127.0.0.1:5000/` in your browser.  
   - Verify that the page loads with styling and clickable social links.  

💡 **Extra Challenge**:  
- Add more sections like "About Me", "Skills", or "Projects".  
- Apply animations to the avatar or icons using CSS transitions.  
- Make the site fully responsive for mobile devices.  
