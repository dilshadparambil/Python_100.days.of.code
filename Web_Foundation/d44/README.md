## Day 44: Motivational Poster Website  
A simple motivational poster-style webpage built with HTML and CSS. This project emphasizes intermediate-level CSS styling, typography, and layout techniques.

📄 [View My Code](my_code/index.html) 📄 [View My Styles](my_code/style.css)  
📄 [View Solution Code](solution/solution.html) 📄 [View Solution Styles](solution/solution.css) 

### 🧠 Concepts Covered
- Linking external CSS stylesheets  
- Importing and using Google Fonts  
- CSS `text-transform` property  
- Applying borders, margins, and alignment  
- Setting full-page background colors  
- Responsive image sizing  
- Centering elements using `margin` and `width`  
- Typography and text styling  

---

### 📝 Instructions
1. **Set up the HTML file**  
   - Create a `div` container to hold an image, a heading (`<h1>`), and a paragraph (`<p>`).  
   - Add an image to the `assets/images` folder and use `<img>` to display it.  
   - Use meaningful text for the heading and description.

2. **Add Google Fonts**  
   - Include the **Libre Baskerville** font using the link from Google Fonts.  
   - Use `<link rel="preconnect">` for optimized font loading.  

3. **Style the Page with CSS**  
   - Set the entire page’s background color to black using the `*` selector.  
   - Make all text white for contrast.  
   - Center-align all text inside the `div`.  
   - Apply the Libre Baskerville font to all text.

4. **Style the Image**  
   - Give the image a **5px solid white border**.  
   - Set the image width to `100%` of the parent container to make it responsive.

5. **Center the Content**  
   - Give the parent `div` a width of `50%` and a left margin of `25%` to center it horizontally.  
   - Add vertical spacing using `margin-top`.

6. **Style the Heading**  
   - Transform the heading text to uppercase using `text-transform: uppercase;`.  
   - Adjust the font size (e.g., `3rem`) for emphasis.

---

💡 **Extra Challenge**:
- Add more motivational posters by duplicating the structure with new images and quotes.  
- Make the layout responsive by using media queries to adjust the `div` width and margins for smaller screens.  
