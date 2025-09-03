#Illustrates simple matplotlib plot

import matplotlib.pyplot as plt
#plt.style.use('classic')

def main():
    x = [i for i in range(-100,100)]
    y = [i*i for i in x] 
    plt.plot(x,y)
    plt.show()
    
main()
    
