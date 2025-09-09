'''
Demonstrates:
1. Calling Functions
2. Local variables
'''

def do_stuff(times):
   for i in range(times):
      print("Hello World")

def main():
   howMany = int(input("Input an integer value for howMany\n"))
   do_stuff(howMany)

if __name__ == "__main__":
   main()
