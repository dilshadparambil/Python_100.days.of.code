### Day 16: Coffee Machine Project (OOP Version)  
An object-oriented simulation of a coffee vending machine that can serve espresso, latte, and cappuccino.  
This version uses **classes** to manage menu items, resources, and transactions.

📄 [View Solution](solution.py) 📄 [View My code](d16.py)  

#### 🧠 Concepts Covered
- Object-Oriented Programming (OOP)  
- Classes and objects  
- Methods and attributes  
- Composition of multiple classes  
- Dictionaries for storing menu data and resources  
- Conditional logic for handling transactions and availability  
- Floating-point arithmetic for currency calculations

#### 📝 Instructions

1. **Prompt user**  
   - Ask: `"What would you like? (espresso/latte/cappuccino):"`  
   - Decide action based on user input.  
   - Show prompt again after each transaction.

2. **Turn off the machine**  
   - If input is `"off"`, end the program.

3. **Print report**  
   - If input is `"report"`, display current resources and money. Example:  
     ```
     Water: 100ml  
     Milk: 50ml  
     Coffee: 76g  
     Money: $2.5
     ```

4. **Check resources**  
   - Ensure enough ingredients are available for the selected drink.  
   - If not, print: `"Sorry there is not enough <resource>."` and skip transaction.

5. **Process coins**  
   - Prompt for number of quarters, dimes, nickles, and pennies.  
   - Calculate total inserted money.

6. **Check transaction**  
   - If inserted amount < drink cost → `"Sorry that's not enough money. Money refunded."`  
   - If enough → Add cost to machine’s profit.  
   - If more than enough → Return change (rounded to 2 decimal places).

7. **Make coffee**  
   - Deduct required ingredients from resources.  
   - Print: `"Here is your <drink>. Enjoy!"`

---

#### 📦 Classes Overview

**`MenuItem` Class**  
- **Attributes**:  
  - `name` (str) → Name of drink (e.g., `"latte"`)  
  - `cost` (float) → Price of drink (e.g., `1.5`)  
  - `ingredients` (dict) → Required ingredients (e.g., `{"water": 100, "coffee": 16}`)  

**`Menu` Class**  
- **Methods**:  
  - `get_items()` → Returns all menu item names as a string (e.g., `"latte/espresso/cappuccino"`)  
  - `find_drink(order_name)` → Returns `MenuItem` object if found, else `None`.

**`CoffeeMaker` Class**  
- **Methods**:  
  - `report()` → Prints resource levels.  
  - `is_resource_sufficient(drink)` → Checks if enough resources for given `MenuItem`.  
  - `make_coffee(order)` → Deducts ingredients for given `MenuItem`.

**`MoneyMachine` Class**  
- **Methods**:  
  - `report()` → Prints current profit.  
  - `make_payment(cost)` → Processes coin input and returns `True` if payment successful, else `False`.

💡 **Extra Challenge**:
- Add an "admin mode" for refilling resources.  
- Implement saving and loading machine state between runs.  
- Allow discounts or promotions.

---
