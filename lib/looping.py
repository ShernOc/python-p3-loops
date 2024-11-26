#!/usr/bin/env python3

#for while loop
def happy_new_year():
      x=10
      while x >= 0:
        if x==0:
            print("Happy New Year!")
        else:
            print(x)
        x -=1

happy_new_year()

# returns the list of squared elements
#use range
square_integers_array =([1, 2, 3, 4, 5])
def square_integers(items):
    return [items**2 for items in square_integers_array]

print(square_integers(square_integers_array))

 
#for in range: 
def fizzbuzz():
    for x in range(1,101): 
        if x % 3 == 0 and x % 5 ==0: 
            print("FizzBuzz")
        elif x % 3==0: 
            print("Fizz")
        elif x % 5 ==0: 
            print("Buzz")
        else: 
            print(x)

fizzbuzz()
