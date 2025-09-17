## Day 43: Color Vocabulary Website  
A simple beginner-friendly HTML and CSS project to learn how to style web pages. This website teaches Spanish color names with images while introducing basic CSS concepts.  

📄 [View My Code](my_code/index.html) 📄 [View My Styles](my_code/style.css)  
📄 [View Solution Code](solution/solution.html) 📄 [View Solution Styles](solution/style.css) 

---

### 🧠 Concepts Covered
- HTML structure and elements  
- Linking an external CSS file to an HTML page  
- Using element **IDs** and **classes** for styling  
- CSS properties:  
  - `color`  
  - `font-weight`  
  - `height`, `width`  
  - Universal selector `*`  
- Center-aligning content with `text-align`  
- Applying consistent styling to multiple elements  

---

### 📝 Instructions

1. **Set Up HTML**  
   - Create an `index.html` file.  
   - Add a title (`<h1>`) and subtitle (`<h2>`).  
   - Add Spanish color names (`Rojo`, `Azul`, `Anaranjado`, `Verde`, `Amarillo`) as `<h2>` elements with `id`s for each color.  
   - Add images for each color using `<img>` tags.  
   - Make sure to include `alt` text for accessibility.  

2. **Connect External CSS**  
   - Create a `style.css` file.  
   - Link it in your HTML `<head>` using:  
     ```html
     <link rel="stylesheet" href="./style.css">
     ```

3. **Style Text by ID**  
   - Use `id` selectors (`#red`, `#blue`, etc.) to match the Spanish color names with their corresponding colors.  
     ```css
     #red { color: red; }
     #blue { color: blue; }
     ```

4. **Set Font Weights**  
   - Apply `font-weight: normal;` to all color titles using the `.color-title` class.  
     ```css
     .color-title { font-weight: normal; }
     ```

5. **Resize Images**  
   - Make all color images **200px x 200px**.  
     ```css
     img { height: 200px; width: 200px; }
     ```

6. **Center the Content**  
   - Use a universal selector to center-align all text:  
     ```css
     * { text-align: center; }
     ```

---

💡 **Extra Challenge:**  
- Add hover effects to the color names (e.g., underline or scale image on hover).  
- Add a background color or border for each color block.  
- Make the layout responsive using CSS Flexbox or Grid.  
