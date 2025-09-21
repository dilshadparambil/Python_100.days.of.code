## Day 54: Create Your Own Python Decorator  
A project where you build a custom decorator to measure the execution time of functions.  

📄 [View Solution](solution.py) 📄 [View My Code](d54.py)  

---

### 🧠 Concepts Covered
- **Decorators (`@`)** → Wrapping functions to extend functionality  
- **Higher-order functions** → Passing functions as arguments  
- **`time.time()`** for execution time measurement  
- **`__name__` attribute** → Identifying function names dynamically  
- **Introduction to Flask-style decorators** → Understanding how `@app.route` works internally  
- **Function wrapping and reusability**  

---

### 📝 Instructions

#### 1. Understand `time.time()`
- Returns the current time in seconds since **Epoch (Jan 1, 1970)**.  
- Example:
```python
import time
print(time.time())
# 1695050908.1985211
```

Run it multiple times → notice the difference = elapsed seconds.  

---

#### 2. Define a Decorator
Create a decorator `speed_calc_decorator()` that:  
1. Takes a function as an argument.  
2. Runs the function.  
3. Calculates execution time.  
4. Prints how long it took.  

```python
import time

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function
```

---

#### 3. Apply the Decorator
Use the `@` syntax to wrap functions:

```python
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
```

---

#### 4. Run Functions
```python
fast_function()
slow_function()
```

**Expected Output**:
```
fast_function run speed: 0.3397s
slow_function run speed: 2.9590s
```

---

#### 5. Explore `__name__`
- Every function in Python has a `__name__` attribute.  
- This helps decorators print which function was executed.  

```python
print(fast_function.__name__)  # fast_function
```

---

💡 **Extra Challenge**:  
- Modify the decorator to handle functions with arguments (`*args, **kwargs`).  
- Return the result of the original function.  
- Create multiple decorators and stack them (`@decorator1 @decorator2`).  

---  
