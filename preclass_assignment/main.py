from functions import greet, goldilocks, square_list, fibonacci_stop, clean_pitch

# Exercise 1 
greet('World')

# Exercise 2
list_of_length = [139, 140, 141, 149, 150, 151, 152]

for length in list_of_length:
    print("Length: " + str(length) + " - " + goldilocks(length))

# Exercise 3
print(square_list([1, 2, 3]))

# Exercise 4
print(fibonacci_stop(30))

# Exercise 5
x = [-1, 2, 6, 95, 55]
status = [1, 0, 0, 0, 1]
x_clean = clean_pitch(x, status)
print(x_clean)

