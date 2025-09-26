#!/usr/bin/env python3

'''
 Name: Simon Field
 Class: CPSC 222, Section 01
 Date Submitted: September 5, 2025
 Assignment: Project 1                 
 Description: This program generates random integers and finds prime numbers from them.
 Sources:
  Python, 9/5/2025, https://docs.python.org/3/library/typing.html
  Python, 9/5/2025, https://docs.python.org/3/library/exceptions.html
  W3Schools, 9/5/2025, https://www.w3schools.com/python/ref_func_range.asp
  W3Schools, 9/5/2025, https://www.w3schools.com/python/ref_exception_valueerror.asp
  GeeksForGeeks, 9/5/2025, https://www.geeksforgeeks.org/python/python-how-to-get-the-last-element-of-list/
'''

import sys
import random

def get_user_input() -> int:
    """Prompt user to enter number from console"""
    while True:
        try:
            n = int(input("Enter a positive integer n: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            return n
        except ValueError:
            print("Please enter a valid integer.")

def generate_random_integers(n: int) -> list:
    """Generate random integers"""
    candPrimes: list = [random.randint(0, n) for _ in range(n)]
    return candPrimes

def get_primes(numbers: list) -> list:
    """Get prime numbers from the given list"""
    realPrimes: list = [n for n in numbers if isPrime(n)]
    return realPrimes

def display(lst: list) -> None:
    """Display list"""
    for element in lst:
        print(element)

def isPrime(num: int) -> bool:
    """Determine if a number is prime"""
    
    if num == 2:
        return True
    if num < 2 or is_even(num):
        return False

    # only need to check up to the sqrt of the number
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    
    # not evenly divisible by anything else, true
    return True

def is_even(num: int) -> bool:
    """Determine if a number is even"""
    return num % 2 == 0

def main():
    """Main function"""
    # prompt user to enter n from console
    n: int = get_user_input()
    
    # generate random integers in the range [0...n]
    candPrimes: list = generate_random_integers(n)
    
    print(candPrimes)

    # select primes from the integers list
    filteredPrimes: list = get_primes(candPrimes)
    
    # display the list of primes on screen, one-at-a-time
    display(filteredPrimes)
    
    # success
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
