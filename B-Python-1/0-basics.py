'''
Demonstrates:
1. Structure of a Python program
2. variables
3. for loop
4. printing to console 
5. type casting
6. console input
'''

#python is profoundly picky about indentation.  I am using 3 spaces here.
#You can use tabs,too, but don't mix them

def main():
   howMany = int(input("Input an integer value for howMany\n"))

   for i in range(howMany):
      print("Hello World")


#allows Python to distinguish running the function directly (our choice here)
#and being imorted

if __name__ == "__main__":
   main()
