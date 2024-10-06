#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!")
    
    
    


def square_integers(int_list):
    new_int_list = list()
    for numbers in int_list:
        numbers = numbers*numbers
        new_int_list.append(numbers)
    return new_int_list
        
    
    

def fizzbuzz():
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else: 
            print(f"{n}")
        

fizzbuzz()

