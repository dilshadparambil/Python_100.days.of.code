## Day 58: TinDog Website  
A responsive landing page built to practice **Bootstrap 5** concepts. The website mimics a dating app for dogs and demonstrates layout, components, and styling features of Bootstrap.

📄 [View My Html](my_code/index.html)  📄 [View Solution Html](solution/solution.html) 

### 🧠 Concepts Covered
- Introduction to **Bootstrap 5**  
- Responsive grid system (`container`, `row`, `col`)  
- Utility classes for spacing, typography, and alignment  
- Bootstrap components: buttons, cards, footer, navigation  
- Icons and SVG integration  
- Using Bootstrap’s responsive images (`img-fluid`)  
- Adding external CSS alongside Bootstrap  

### 📝 Instructions
1. **Set up Bootstrap in your project**  
   - Link the Bootstrap CSS in the `<head>` section.  
   - Add a custom stylesheet (`style.css`) for additional styling.  

2. **Create the Title Section**  
   - Use a Bootstrap grid (`row`, `col`) to split the section into two parts:  
     - Left: App text and download buttons.  
     - Right: Phone image (`img-fluid` for responsiveness).  
   - Add gradient background for styling.  

3. **Add the Features Section**  
   - Use a 3-column responsive grid with Bootstrap’s `row-cols-lg-3`.  
   - Include icons (`bi-` classes) and text for features like *Easy to Use*, *Elite Clientele*, and *Guaranteed to Work*.  

4. **Testimonial Section**  
   - Create a centered quote section with background.  
   - Add an image for the user testimonial.  
   - Display brand logos in a responsive row.  

5. **Pricing Section**  
   - Use Bootstrap **cards** (`card`, `card-body`, `card-header`).  
   - Create 3 pricing tiers (Chihuahua, Labrador, Mastiff).  
   - Add buttons styled with `btn-outline-dark` or `btn-dark`.  

6. **Footer Section**  
   - Use Bootstrap’s grid layout for multiple columns.  
   - Include navigation links and copyright.  

7. **Make the Website Responsive**  
   - Test across multiple screen sizes.  
   - Ensure all images use `img-fluid`.  
   - Use utility classes like `text-center`, `mx-auto`, `mb-3`, `mt-5` for spacing and alignment.  

💡 **Extra Challenge**:
- Add a **Bootstrap Navbar** at the top with scroll-to sections.  
- Include animations using Bootstrap’s utilities or external libraries.  
- Customize Bootstrap variables for brand colors.  
