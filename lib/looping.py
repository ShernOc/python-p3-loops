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
def square_integers(int_list):
    return [square**2 for square in int_list]
result = square_integers([5,2,4])
print(result)

    

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
