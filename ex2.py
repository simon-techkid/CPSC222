'''
Demonstrates:
1. List (done the non-pythonic way) 
'''

def do_stuff(times):
   lst = []
   for i in range(times):
     lst.append(i)
   return lst

def main():
   howMany = 10
   lst = do_stuff(howMany)
   print(lst) 

if __name__ == "__main__":
   main()
