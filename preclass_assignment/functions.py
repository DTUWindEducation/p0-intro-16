# Exercise 1 : Write a simple function
def greet(name):
    return print("Hello, " + name + "!")



# Exercise 2 : If/Else statements
def goldilocks(length):
    if length > 150:
        return "Too large!"
    elif length < 140:
        return "Too small!"
    else:
        return "Just right! :)"



# Exercise 3 : For loops
def square_list(list):
    return [x**2 for x in list]


# Exercise 4 : While loops
def fibonacci_stop(stop):
    fib = [0, 1]
    while fib[-1] < stop:
        fib_new = fib[-1] + fib[-2]
        fib.extend([fib_new])
    return fib[:-1]


# Exercise 5 : Local operators

def clean_pitch(x, status):
    x_clean = [None] * len(x)
    for i in range(len(x)):
        if x[i] < 0 and status[i] == 1:
            x_clean[i] = -999
        elif x[i] < 0 and status[i] == 0:
            x_clean[i] = x[i]
        elif x[i] > 90 and status[i] == 1:
            x_clean[i] = -999
        elif x[i] > 90 and status[i] == 0:
            x_clean[i] = x[i]
        else:
            x_clean[i] = x[i]
    return x_clean
