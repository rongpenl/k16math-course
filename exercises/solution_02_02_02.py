import matplotlib.pyplot as plt # this line has to be here if you want to do some plotting, for now.
def xToY(x):
    return x*x+x-1
X = [ -2, -1, 0, 1, 2]
Y = [xToY(x) for x in X]

plt.plot(X,Y)