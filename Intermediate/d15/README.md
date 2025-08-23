## Day 15: Coffee Machine Project  
A simulation of a coffee vending machine that can serve espresso, latte, and cappuccino.  
The program manages resources, processes coins, and handles transactions.

📄 [View Solution](solution.py) 📄 [View My code](d15.py)  

### 🧠 Concepts Covered
- Using **dictionaries** to store menu items, prices, and resources  
- Creating **functions** for modular tasks (report generation, resource check, transaction check, making coffee)  
- Using **loops** for continuous machine operation until turned off  
- Applying **conditional statements** to handle different commands (`off`, `report`, drink orders)  
- Performing **floating-point calculations** for money handling  
- **Rounding values** when returning change to customers  

### 📝 Instructions
1. **Prompt the User**  
   - Ask: `"What would you like? (espresso/latte/cappuccino):"`  
   - Process the input and take the appropriate action.  
   - After serving a drink or completing another task, re-display the prompt for the next customer.  

2. **Turn Off the Machine**  
   - If the user types `"off"`, terminate the program immediately.  
   - This serves as a hidden feature for maintainers.  

3. **Print Report**  
   - If the user types `"report"`, display the current status of machine resources:  
     ```
     Water: 100ml  
     Milk: 50ml  
     Coffee: 76g  
     Money: $2.5
     ```

4. **Check Resource Availability**  
   - When a drink is requested, verify if all required resources are sufficient.  
   - If any resource is lacking, print:  
     `"Sorry, there is not enough <resource>."`  
   - Cancel the order and return to the prompt.  

5. **Process Coins**  
   - If resources are sufficient, ask the user to insert coins.  
   - Accept coins in the following denominations:  
     - Quarters = $0.25  
     - Dimes = $0.10  
     - Nickles = $0.05  
     - Pennies = $0.01  
   - Calculate the total amount of money inserted.  

6. **Validate Transaction**  
   - If total money < drink cost → print `"Sorry, that's not enough money. Money refunded."`  
   - If total money ≥ drink cost →  
     - Add the drink’s cost to the machine’s profit.  
     - If excess money was provided, return change rounded to **2 decimal places**.  

7. **Make Coffee**  
   - Deduct the required ingredients from machine resources.  
   - Print a message to confirm: `"Here is your <drink>. Enjoy!"`  
   - Example before purchasing a latte:  
     ```
     Water: 300ml  
     Milk: 200ml  
     Coffee: 100g  
     Money: $0
     ```
     Example after purchasing a latte:  
     ```
     Water: 100ml  
     Milk: 50ml  
     Coffee: 76g  
     Money: $2.5
     ```

💡 **Extra Challenge**  
- Add more drink options (e.g., mocha, americano).  
- Implement an admin password to access the report.  
- Track and display the number of drinks sold per type.  
