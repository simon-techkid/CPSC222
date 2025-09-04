'''
Demonstrates:  file i/o
'''
import sys 

def file_read(fin):
   poem = ''
   with open(fin, 'r') as f:
      ch = f.read()
      while ch:
         poem = poem + ch 
         ch = f.read()

   print("\nFile read successfully")
   return poem

def file_write(fout,poem):
   poem = [ch.upper() if ch.islower() else ch for ch in poem] 
   with open(fout,'w') as f:
      for ch in poem:
         f.write(ch) 

   print("\nFile written successfully")
   return poem

def main():
    fin = sys.argv[1]
    fout = sys.argv[2] 
    poem = file_read(fin) 
    file_write(fout,poem)


if __name__ == "__main__":
  main()     
