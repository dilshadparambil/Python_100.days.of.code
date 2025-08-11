### Day 9: Blind Auction   
A program to run a **blind auction**, where participants enter their names and bids privately.  
The program determines the highest bidder without revealing intermediate bids.

📄 [View Solution](solution.py) 📄 [View My code](d9.py)  

#### 🧠 Concepts Covered
- Dictionaries (`{key: value}`)  
- Nesting data inside structures  
- Loops for repeated user input  
- Clearing output to maintain bid privacy  
- Converting strings to integers (`int()`)

#### 📝 Instructions
1. Ask each participant for:
   - **Name**
   - **Bid amount**
2. Save each bid in a dictionary:
   ```python
   bids = {
       "Alice": 250,
       "Bob": 300
   }
3. Ask if there are more participants:
   - If yes → Clear the screen (e.g., print("\n" * 20)) and repeat the bidding process.
   - If no → Determine the highest bidder.
4. Announce the winner and their winning bid.

 **📌 Functional Requirements**
   - Data storage: Use a dictionary where the key = bidder’s name, value = bid amount.
   - Comparison: Find the maximum bid value and print the name of the bidder.
   - Privacy: Ensure no previous bids are visible when the next participant enters their bid.
   - Flow: Continue looping until no more bids are to be entered.

Use this [flowchart](d9flow.png) to design your Blind Auction

**💡 Hints:**
   - Draw a flowchart to visualize the program’s logic before coding.
   - Convert all bid inputs to integers for correct comparison:

---