import numpy as np       # imports package for scientific computing under name: “np”
import matplotlib.pyplot as plt       # package for plotting
import scipy       # package for crunching numbers
x=np.linspace(-2.5,1,1000)         # creates empty array of length 1000 in range [-2.5, 1]
y=np.linspace(-1.5,1.5,1000)      # same as above line, but for the y-coordinate 
a,b = np.meshgrid(x,y)               # creates grid of dimensions (x, y) 
c=a+1j*b                                  # c is a complex number ( j is standard for comp. Sci., but i is used in mathematics)
maxiterations=100                              # maximum number of iterations
def mandelbrot_set(c, maxiterations): # function takes complex number, c, and maxiter. value
	emptystartinggrid=np.zeros(1000000)        # creates an array full of zeroes that is length 1000000
	z = emptystartinggrid        # rename the variable to something shorter
	z=z.reshape(1000,1000)    # re-formats to be an array of dimension 1000 x 1000
	zz=np.copy(z)                   # zz is a copy of the 1000 x 1000 array, that we will put values that diverge
	for n in range(1, maxiterations):  # iterates 100 times (depending on what maxiter is)
		z=z**2+c                # squares a value in grid of z and adds a complex number according to the function fc(z)
		index=np.where(abs(z)>2)   # search for indices where |z| > 2 (diverges)
		zz[index]=n         # for indices in which |z| > 2 (which values of z diverge), and put these values into the list zz, then take this point, z, and make it n, and see if z (the sum) diverges again
	return zz                    # return the list, zz, with values of |z| > 2
plt.imshow(np.sqrt(mandelbrot_set(c,maxiterations)), cmap='viridis_r')   # plots sqrt(zz)
plt.title("Mandelbrot Set")
plt.xlabel("Re[c] (the real part of set c)")
plt.ylabel("Im[c] (the imaginary part of set c)")
ax=plt.subplot(111)
t = plt.text(0.06, 0.94, 'c = a number in the complex plane', transform=ax.transAxes, fontsize=12)
t.set_bbox(dict(facecolor='white', alpha=0.95, edgecolor='white'))
plt.show()       # show the plot
plt.clf()           #close all plots