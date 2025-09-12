## Day 31: Flash Card App  
A flash card application to learn French words using a spaced-repetition-style workflow.  
The program shows a French word, flips to reveal its English translation after a delay, and lets users mark words as known so they don’t reappear.  

📄 [View Solution](solution/solution.py) 📄 [View My Code](my_code/d31.py)  

### 🧠 Concepts Covered
- Tkinter GUI for building interactive desktop apps  
- Tkinter `Canvas` to display images and layered text  
- Tkinter `Button` with `PhotoImage` icons  
- Event scheduling with `after()` and cancellation with `after_cancel()`  
- Persistent state with CSV files  
- Pandas for reading/writing tabular data (`read_csv`, `to_csv`)  
- Converting DataFrames to dicts with `to_dict(orient="records")`  
- Basic app state management (current card, timer handle, remaining words)  

### 📝 Instructions

#### Step 1 — Create the User Interface (UI) with Tkinter
1. **Project assets**  
   - Ensure you have `images/` containing: `card_front.png`, `card_back.png`, `right.png` (✅), `wrong.png` (❌).  
   - Ensure you have `data/french_words.csv` (with columns `French,English`).  
2. **Window setup**  
   - Create the main window (`Tk()`), set title (e.g., “Flashy”), apply padding (e.g., `padx=50`, `pady=50`).  
   - Configure background color to match your card theme (commonly white).  
3. **Canvas (flash card)**  
   - Create a `Canvas` sized to the card art (e.g., `width=800`, `height=526`).  
   - Load images using `PhotoImage(file="images/card_front.png")` and `PhotoImage(file="images/card_back.png")`.  
   - Add the card front image with `create_image(x, y, image=card_front_img)`.  
   - Add two text items:  
     - Title text at top (e.g., “French”),  
     - Word text centered (large font).  
   - **Important:** Keep `PhotoImage` objects in module/global scope (not inside functions) so they are not garbage-collected.  
4. **Buttons**  
   - Create ❌ (wrong) and ✅ (right) buttons below the card using `PhotoImage` icons (`images/wrong.png`, `images/right.png`).  
   - Set `highlightthickness=0` and place them with `.grid()` (e.g., columns 0 and 1).  
5. **Layout**  
   - Use a 2×2 grid: the `Canvas` spans 2 columns; buttons sit below in their own columns.  
   - Ensure consistent padding and alignment.

#### Step 2 — Create New Flash Cards
1. **Load words**  
   - Read `data/french_words.csv` into a DataFrame, then convert to a list of records:  
     `records = df.to_dict(orient="records")` which yields `[{ "French": "chaque", "English": "each" }, ...]`.  
2. **Pick a random card**  
   - Implement a function (e.g., `next_card()`) that:  
     - Cancels any existing flip timer (`after_cancel`) if set.  
     - Randomly selects a record from your remaining list.  
     - Updates canvas to **front side**:  
       - Image: `card_front.png`  
       - Title: “French” (e.g., black text)  
       - Word: the selected French word  
     - Schedules a flip in 3 seconds: `flip_timer = window.after(3000, flip_card)`.  
3. **Button bindings**  
   - ❌ button calls `next_card()` (user doesn’t know the word → show another).  
   - ✅ button calls a handler to mark the word as known (see Step 4), then `next_card()`.

#### Step 3 — Flip the Cards!
1. **Flip logic**  
   - Implement `flip_card()` to reveal the translation:  
     - Change canvas image to `card_back.png`.  
     - Update title to “English”.  
     - Update word text to the English translation.  
     - Change text color to white for readability on the back image.  
2. **Timer handling**  
   - Every time a new card is shown (❌/✅ pressed), cancel the previous flip if pending using `after_cancel(flip_timer)` before scheduling a new one.

#### Step 4 — Save Your Progress
1. **Remove known words**  
   - When ✅ is pressed, remove the current record from your in-memory list of words still to learn.  
2. **Persist to CSV**  
   - Write the remaining words to `data/words_to_learn.csv` using `to_csv(..., index=False)`.  
   - Do this whenever the user marks a word known (or at sensible checkpoints).  
3. **Load progress on start**  
   - On startup, try to read `data/words_to_learn.csv`.  
     - If it exists and has data, use that as your working list.  
     - Otherwise, fall back to the original `french_words.csv`.  
4. **End conditions**  
   - If the remaining list becomes empty, optionally show a congratulatory message and disable buttons.

#### Quality-of-Life Notes
- Keep references to canvas text IDs and image IDs so you can update them efficiently with `itemconfig(...)`.  
- Use consistent fonts (e.g., a large bold font for the word, smaller for the title).  
- Consider a subtle background color or margins to match the card art.

💡 **Extra Challenges**
- Add a “Reset Progress” button that restores from `french_words.csv`.  
- Track session stats (correct/incorrect counts).  
- Add multiple language decks with a dropdown.  
- Implement spaced-repetition weighting (e.g., show unknown words more frequently).  
