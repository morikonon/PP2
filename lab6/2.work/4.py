import time
from math import sqrt

def invoke_sqrt_after_milliseconds(number, milliseconds):
    seconds = milliseconds / 1000
    
    time.sleep(seconds)
    
    result = sqrt(number)
    
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

number = 25100
milliseconds_delay = 2123

invoke_sqrt_after_milliseconds(number, milliseconds_delay)