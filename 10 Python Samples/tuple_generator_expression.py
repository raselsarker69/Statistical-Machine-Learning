tuple1 = range(1, 11)

even_sqr = (x ** 2 for x in tuple1 if x % 2 == 0)    # even squares
odd_sqr = (x ** 2 for x in tuple1 if x % 2 != 0)     # odd squares
double_num = (x * 2 for x in tuple1 if x % 2 != 0)   # double of odd numbers
 
print(tuple(even_sqr))
print(tuple(odd_sqr))
print(tuple(double_num))
