## Day 45: Top 100 Movies List (Web Scraping)  
A Python script that scrapes the top 100 movies of all time from a website and stores them in a text file.  
This project focuses on **web scraping** fundamentals using `requests` and `BeautifulSoup`.

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d45.py) 

### 🧠 Concepts Covered
- Sending HTTP GET requests using the `requests` library  
- Parsing and navigating HTML content using `BeautifulSoup`  
- Selecting HTML tags and attributes with `.find()` and `.find_all()`  
- Extracting and cleaning text from HTML elements  
- Writing data to `.txt` files  
- Python lists, loops, and string manipulation  
- Understanding website structure (HTML tags, classes, and IDs)  

---

### 📝 Instructions
1. **Choose a Target Website**  
   - Use a movie-ranking website (e.g., Empire, IMDb, or Rotten Tomatoes).  
   - Inspect the page structure using browser developer tools (`Right Click > Inspect`) to identify tags containing movie titles.

2. **Send an HTTP Request**  
   - Use the `requests` library to send a GET request to the website URL.  
   - Retrieve the HTML content of the page.

3. **Parse the HTML Content**  
   - Initialize a `BeautifulSoup` object with the HTML response.  
   - Use `soup.find_all()` to select the HTML elements containing movie titles.  

4. **Extract Movie Titles**  
   - Loop through the selected elements and extract movie names as text.  
   - Clean up whitespace or extra characters using `.getText()` or `.strip()`.

5. **Store Titles in a List**  
   - Save all extracted titles into a Python list.  
   - Optionally reverse the order if the website lists movies from best to worst.

6. **Write Titles to a File**  
   - Open a `.txt` file in write mode.  
   - Write each movie title on a new line.

7. **Run the Script**  
   - Execute the script to generate a `movies.txt` file containing the top 100 movies.

---

💡 **Extra Challenge**:
- Add ranking numbers next to each title in the file.  
- Scrape additional details (e.g., release year or director) and include them in the output.  
- Convert the list into a JSON or CSV file for structured storage.  
