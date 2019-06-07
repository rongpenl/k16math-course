# those two lines have to be here if you want to do some plotting, for now.
import matplotlib.pyplot as plt 
%matplotlib inline


def xToY(x):
    return x*x+x-1
X = [ -2, -1, 0, 1, 2]
Y = [xToY(x) for x in X]
plt.grid()
plt.plot(X,Y)
plt.show()

# Let's have a finer plotting

X = [0.01*i for i in range(-200,201,1)]
Y = [xToY(x) for x in X]
plt.grid()
plt.plot(X,Y)