'1. Write a simple function'

greet = ('Dimi')  # Define a function called greet that takes a name as a string
print('Hello,', greet,"!")  # print "Hello, <name>!" 


'2. If/else statements'

def goldilocks(bed_length):        # Goldilocks is 135 cm tall
    if bed_length < 140:           # If the bed is shorter than 140 cm, or larger than 150 cm, then she is unhappy
        print("Too small! ")
    elif bed_length > 150:
        print("Too large!")
    else:
        print("Just right. :)")
        
goldilocks(140)


'3. For loops'

import numpy as np     
def square_list(x,y,z):                             #  takes a list of numbers and returns a list where each element has been squared
   """Calculate the squares of x,y,z"""
   return np.array([np.square(x),np.square(y),np.square(z)])

x, y, z = 1, 2, 3 
print(square_list(x,y,z))


'4. While loops'


def fibonacci_stop(max_value):
    """Return a list of Fibonacci numbers up to max_value."""
    fib_sequence = []  # Start with an empty list
    x, y = 1, 1        # First two Fibonacci numbers
    
    while x <= max_value:
        fib_sequence.append(x)  # Append the current Fibonacci number to the list
        x, y = y, x + y         # Update the values for the next iteration
    
    return fib_sequence

print(fibonacci_stop(30))  


"5. Logical operators"

def clean_pitch(pitches, statuses):
    
    """ Clean pitch measurements based on instrument status.
    
    For each pitch measurement:
      - If the pitch is outside [0, 90] and the corresponding status is non-zero (instrument malfunctioning), the pitch is set to -999.
      - Otherwise, the pitch is left unchanged.
    
    Parameters:
        pitches (list of numbers): The pitch measurements.
        statuses (list of numbers): The corresponding status signals.
    
    Returns:
        list: The cleaned pitch measurements. """
        
    cleaned = []
    for pitch, status in zip(pitches, statuses):
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned.append(-999)
        else:
            cleaned.append(pitch)
    return cleaned

# Example usage:
x = [-1, 2, 6, 95]       # "raw" pitch angles at four time steps
status = [1, 0, 0, 0]    #  status signal

print(clean_pitch(x, status))  # Output: [-999, 2, 6, 95]
