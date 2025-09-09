'''
Demonstrates:
List Comprehension 
'''

def do_stuff(size):
   lst = [i for i in range(size)]
   return lst

def main():
   howMany = 10
   lst = do_stuff(howMany)
   print(lst) 

if __name__ == "__main__":
   main()
