## Day 46: Music Time Machine  
A Python project that creates a Spotify playlist of Billboard Hot 100 songs from a specific date entered by the user.  
It uses **web scraping** to extract the Billboard chart and **Spotify API** to create playlists dynamically.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d46.py) 

### 🧠 Concepts Covered
- Web scraping with `requests` and `BeautifulSoup`  
- Spotify API integration with `spotipy`  
- OAuth authentication for accessing Spotify account  
- Extracting and cleaning HTML data  
- Automating playlist creation  
- Working with Python lists and loops  
- String formatting and user input handling  

---

### 📝 Instructions
1. **Set Up Spotify Developer Account**  
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).  
   - Create a new app and note down the `Client ID`, `Client Secret`, and `Redirect URI`.  
   - Add your `Redirect URI` in your app settings.  

2. **Install Required Libraries**  
   - Install `spotipy` for Spotify API integration:  
     ```bash
     pip install spotipy
     ```
   - Install `requests` and `beautifulsoup4` for web scraping:  
     ```bash
     pip install requests beautifulsoup4
     ```

3. **Ask for a Date**  
   - Prompt the user to enter a date in the format `YYYY-MM-DD`.  
   - Example: `2000-08-12`.

4. **Scrape Billboard Hot 100**  
   - Construct the Billboard URL using the entered date:  
     ```
     https://www.billboard.com/charts/hot-100/<YYYY-MM-DD>
     ```
   - Use `requests.get()` to fetch the HTML page.  
   - Parse with `BeautifulSoup` and extract song titles.  
   - Store all 100 song titles in a Python list.

5. **Authenticate with Spotify**  
   - Use `spotipy.SpotifyOAuth` to authenticate with your Spotify account.  
   - Save authentication tokens securely.  

6. **Search for Songs on Spotify**  
   - For each song in the scraped list, search Spotify for a track match.  
   - Store the URIs of found tracks.  
   - Skip songs that are not found on Spotify.

7. **Create a Playlist**  
   - Name the playlist something like `Billboard 100 - YYYY-MM-DD`.  
   - Add all the found track URIs to this playlist using Spotify API.

8. **Run and Test the Script**  
   - Execute your Python script.  
   - Check your Spotify account for the newly created playlist.  

---

💡 **Extra Challenge**:
- Allow the user to select a different chart (e.g., Top 200 or Genre-specific).  
- Save the playlist details (title, tracks, URIs) to a `.csv` or `.json` file.  
- Add error handling for authentication and missing songs.  
