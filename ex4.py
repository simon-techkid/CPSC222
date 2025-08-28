'''
Demonstrates:
1. pseudo-random integers 
2. Conditional statements 
'''

import random

def do_stuff(size):
   lst = [random.randint(0,10) for i in range(10)]
   return lst

def main():
   howMany = 10
   lst = do_stuff(howMany)
   num = random.randint(0,10)
   print("Num = " + str(num))
   if num in lst:
      print(True)
   else:
      print(False)

   #More pythonically
   print(num in lst)
   print(lst)

if __name__ == "__main__":
   main()
