'''
Demonstrates:
1. lst comprehension 
2. for item in construction 
'''

import random

def do_stuff(size):
   lst = [random.randint(0,size) for i in range(size)]
   return lst

def is_even(item):
   if (not item % 2):
    return item


def main():
   howMany = 100
   lst = do_stuff(howMany)

   even_lst = [num for num in lst if is_even(num)]
   print(even_lst) 


if __name__ == "__main__":
   main()
