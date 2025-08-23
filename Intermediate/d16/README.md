## Day 16: Coffee Machine Project (OOP Version)  
An object-oriented simulation of a coffee vending machine that can serve espresso, latte, and cappuccino.  
This version uses **classes** to manage menu items, resources, and transactions.

📄 [View Solution](solution.py) 📄 [View My code](d16.py)  

### 🧠 Concepts Covered
- Object-Oriented Programming (OOP) principles  
- Designing and using **classes and objects**  
- Defining and using **methods and attributes**  
- Composition: how multiple classes interact together  
- Using **dictionaries** to store menu data and resources  
- Applying **conditional logic** for transaction handling and resource availability  
- Performing **floating-point arithmetic** for accurate money handling  

### 📝 Instructions
1. **Prompt the User**  
   - Ask: `"What would you like? (espresso/latte/cappuccino):"`  
   - Process the input and execute the corresponding action.  
   - Continue prompting after each transaction.  

2. **Turn Off the Machine**  
   - If the user enters `"off"`, terminate the program.  

3. **Print Report**  
   - If the user enters `"report"`, display the machine’s current resource levels and profit:  
     ```
     Water: 100ml  
     Milk: 50ml  
     Coffee: 76g  
     Money: $2.5
     ```

4. **Check Resource Availability**  
   - Verify that sufficient resources are available for the requested drink.  
   - If any ingredient is lacking, display:  
     `"Sorry, there is not enough <resource>."`  
   - Cancel the order if resources are insufficient.  

5. **Process Coins**  
   - Ask the user to input the number of quarters, dimes, nickles, and pennies.  
   - Calculate the total money inserted.  

6. **Validate Transaction**  
   - If total money < drink cost → print `"Sorry that's not enough money. Money refunded."`  
   - If total money ≥ drink cost →  
     - Add the cost of the drink to the machine’s profit.  
     - If overpaid, return change rounded to **2 decimal places**.  

7. **Make Coffee**  
   - Deduct the required ingredients from the machine’s resources.  
   - Confirm the order: `"Here is your <drink>. Enjoy!"`  

### 📦 Classes Overview
1. **`MenuItem` Class**  
   - **Attributes**:  
     - `name` → The drink’s name (e.g., `"latte"`)  
     - `cost` → The drink’s price (e.g., `1.5`)  
     - `ingredients` → Dictionary of required ingredients (e.g., `{"water": 100, "coffee": 16}`)  

2. **`Menu` Class**  
   - **Methods**:  
     - `get_items()` → Returns all available menu items as a string (e.g., `"latte/espresso/cappuccino"`)  
     - `find_drink(order_name)` → Searches for a drink and returns its `MenuItem` object if found, else `None`.  

3. **`CoffeeMaker` Class**  
   - **Methods**:  
     - `report()` → Prints remaining resources.  
     - `is_resource_sufficient(drink)` → Checks if enough ingredients are available.  
     - `make_coffee(order)` → Deducts resources and serves the drink.  

4. **`MoneyMachine` Class**  
   - **Methods**:  
     - `report()` → Prints the current profit.  
     - `make_payment(cost)` → Handles coin input and returns `True` if payment is successful, otherwise `False`.  

💡 **Extra Challenge**  
- Add an **admin mode** to allow refilling resources.  
- Save and load the machine’s state between program runs.  
- Add discount codes or promotions for specific drinks.  
