squares_list = [x**2 for x in range(10)]
squares_gen = (x**2 for x in range(10))

print(squares_list)
print(squares_gen)

# list comprehension creates the list immediately but the generator only creates the method to generate the next number nd when it 
# called it will show the required results instead of using up a lot of memory