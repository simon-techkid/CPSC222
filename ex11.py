

import matplotlib.pyplot as plt

import math

def plot_zipf(x,y,xx,yy):
    pl = plt.gca()
    #pl.plot(x,y)
    pl.plot(xx,yy)
    pl.set_xlabel("Rank")
    pl.set_ylabel("Probability")
    #pl.plot("b",x,y)
    plt.show()
        
   
def main():
        x = [i for i in range (1,500)]
        y = [1/i for i in x]
        xx = [math.log(i) for i in x]
        yy = [math.log(i) for i in y]
        plot_zipf(x,y,xx,yy)
    
    
main()
