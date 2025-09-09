'''
Demonstrates:
Naive Counting, pass 1
Items to Note:
1. unpacking operator  *lst
2. Use of enumerate() in a for loop
'''

import random

def do_stuff(howMany, limit):
   #Let howMany = 10, limit = 5
   #randint produces an inclusive interval:[0..5] or 0 .. 5
   #range is inclusive on the left but exclusive on the right: [0,10) or 0 .. 9
   lst = [random.randint(0,limit) for i in range(howMany)]
   
   #We use a list to keep track of how many of each number generated.  Since the numbers 
   #can be 0,1,2,3,4,5 we need 6 slots
   #pos 0 keeps track of 0's
   #pos 1 keeps track of 1's
   #...
   #pos 5 keeps track of 5's
   #Initialize the positions to 0
   results = [0 for i in range(limit+1)] #list of 0's
   
   
   #Do the counting
   #For each possible number, go through the list, incrementing the position
   #in the result list for each match
   for i in range (limit + 1):
      for item in lst:
         if item == i:
           results[i] = results[i] + 1
      
   return(lst,results)
   


def main():
   howMany = int(input("How many random integers?\n")) 
   limit = int(input("Largest random integers >= 0?\n")) 
   
   lst, results = do_stuff(howMany,limit)
   print("Raw List of ", int(howMany)," random integers by value: ", *lst) #notice the unpacking operator
   
   print("Count of Each Possible Integer")
   for i, val in enumerate(results): 
      print(f"{i}: {val}")  #f says to evaluate expression in this string
  


if __name__ == "__main__":
   main()
