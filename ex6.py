'''
Demonstrates:
1. Sets and set oprations 
2. Printing in two ways
'''


def do_stuff():
    fruits = {'apple', 'bannana', 'cherry'}
    moreF = {'bannana', 'orange', 'kiwi'}
    return fruits, moreF

def operations(fruits,moreF):
    print("Union:", fruits | moreF)
    print("Intesection:", fruits & moreF)
    print("Difference;", fruits - moreF) 

def main():
   fruits, moreF = do_stuff()
   fruits.add('lemon')
   print("Fruits: " + str(fruits))
   print("Other Fruits: " + str(moreF))

   operations(fruits,moreF)

   print('apple' in fruits)
   fruits.discard('apple')
   print('apple' in fruits)

if __name__ == "__main__":
   main()
