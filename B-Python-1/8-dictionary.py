'''
Demonstrates: 
dictionary
'''


def do_stuff():
   dict = {}
   dict[0] = "Paul"
   dict[1] = "Heidi"
   dict[2] = "Katie"
   dict[3] = "Simcha"
   dict[4] = "Rosie"
   
   print(dict.keys())
   print(dict.values())
   print(dict.items()) #prints every entry as a tuple
     
   print(dict[3])

   return dict

def main():
   dict = do_stuff()
   for item in dict.items():
      print(f"{item[0]}: {item[1]}")  #f says to evaluate expression in this string
	

if __name__ == "__main__":
   main()
    
    
