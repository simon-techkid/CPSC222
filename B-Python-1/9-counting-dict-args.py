'''
Demonstrates: 
1. Command line arguments
2. Using a dictionary
3. sorting a dictionary using a library
'''

import sys
import random
from operator import itemgetter

def do_stuff(howMany,limit):
   lst = [random.randint(0,limit) for i in range(howMany)]
   print(lst)
    
   count_dict = {}
   for num in lst:
      if num in count_dict:
         count_dict[num] = count_dict[num] + 1
      else:
         count_dict[num] = 1

   #sort the items by the number of times they occur, with highest occurence on top
   sorted_lst = sorted(count_dict.items(), key = itemgetter(1), reverse = True)
   return sorted_lst
    
def main():
   howMany = int(sys.argv[1])
   limit = int(sys.argv[2])
    
   lst = do_stuff(howMany, limit)
   
   print("Occurance of Numbers by Rank")
   for i, item in enumerate(lst):
      print(f"{i+1}:   {item[0]} occurs {item[1]} time(s)")  
      
if __name__ == "__main__":
   main()
    
