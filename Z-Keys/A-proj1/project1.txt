'''
 Name: Paul De Palma
 Class: CPSC 222
 Date Submitted: September 6, 2025
 Assignment: Project 1 Key                                                                  
 Description: Generates random integers and determines if they are prime
'''

import random
import math

'''
Description: Determines whether an integer is prime
Input: integer whose primality is to be judged
Returns: True if input is prime, false otherwise
'''

def isPrime(num):
   for i in range (2,num):
      if num % i == 0:
        return False
   return True

'''
Extra Credit
def isPrime(num):
   i = 2
   while(i <= math.sqrt(num)):
      if num % i == 0:
         return False
      i = i + 1
   return True
'''


'''
Description: Loops over all candidate primes, invoking isPrime on each,  
             storing primes in a list.  Returns list of primes
input: list of candidate primes
output: list of primes
'''
def display(cand_primes):
   #-3 points for students who do not use a list comprehension
   primes = [i for i in range(2, len(cand_primes)) if isPrime(i)];
   for num in primes:
      print(num)

def main():
   nums = int(input("Input the number of random integers\n"))
   print()
   #-3 points for students who do not use a list comprehension
   cand_primes = [random.randint(0,nums) for i in range(nums)]
   display(cand_primes)
  

if __name__ == "__main__":
   main()
