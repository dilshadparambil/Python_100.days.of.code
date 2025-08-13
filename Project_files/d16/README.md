### Day 15: Coffee Machine Project  
A simulation of a coffee vending machine that can serve espresso, latte, and cappuccino.  
The program manages resources, processes coins, and handles transactions.

📄 [View Solution](solution.py) 📄 [View My code](d15.py)  

#### 🧠 Concepts Covered
- Dictionaries for storing menu items and resources  
- Functions for modular code (report generation, resource check, transaction check, coffee making)  
- Loops for continuous operation until turned off  
- Conditional statements for different machine commands  
- Floating-point calculations for money handling  
- Rounding for change calculations

#### 📝 Instructions

1. **Prompt user**:  
   - Ask: `"What would you like? (espresso/latte/cappuccino):"`  
   - Check the input and decide the next action.  
   - After serving a drink or completing an action, show the prompt again for the next customer.

2. **Turn off the machine**:  
   - If the user types `"off"`, stop the program.

3. **Print report**:  
   - If the user types `"report"`, display current resources:  
     ```
     Water: 100ml  
     Milk: 50ml  
     Coffee: 76g  
     Money: $2.5
     ```

4. **Check resources sufficient?**  
   - Before making a drink, check if there are enough ingredients.  
   - If any resource is insufficient, print:  
     `"Sorry there is not enough <resource>."`  
   - Do not proceed with the order.

5. **Process coins**:  
   - If resources are enough, ask for coins:  
     - Quarters = $0.25  
     - Dimes = $0.10  
     - Nickles = $0.05  
     - Pennies = $0.01  
   - Calculate total money inserted.

6. **Check transaction successful?**  
   - If money < drink cost → print `"Sorry that's not enough money. Money refunded."`  
   - If money ≥ drink cost → add cost to machine’s profit.  
   - If money > drink cost → return change, rounded to 2 decimal places.

7. **Make coffee**:  
   - Deduct required resources from machine.  
   - Print: `"Here is your <drink>. Enjoy!"`  
   - Example before buying latte:  
     ```
     Water: 300ml  
     Milk: 200ml  
     Coffee: 100g  
     Money: $0
     ```
     After buying latte:  
     ```
     Water: 100ml  
     Milk: 50ml  
     Coffee: 76g  
     Money: $2.5
     ```

💡 **Extra Challenge**:
- Add more drink options to the menu.  
- Implement an admin password for accessing reports.  
- Track total drinks sold per type.

---
