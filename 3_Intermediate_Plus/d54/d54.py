# Python Decorator

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    start=time.time()
    function()
    stop=time.time()
    print(stop-start)
    return function    
    
    
        
@speed_calc_decorator
def fast_function():

    for i in range(1000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    
    for i in range(10000000):
        i * i
