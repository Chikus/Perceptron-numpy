import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

x = np.arange(-5,5)
x1 = [0]*10
y = np.arange(-5,5)
y1 = [0]*10

fig = plt.figure(figsize=(20,10))

ax = fig.add_subplot(1,1,1)
ax.plot(x,x1)
ax.plot(y1,y)
ax.grid(True)

cordx = []
cordy = []

ref = [[]]
total_size = 0

axcla1 = plt.axes([0.75, 0.01, 0.1, 0.075])
axcla2 = plt.axes([0.86, 0.01, 0.1, 0.075])
axcal = plt.axes([0.64, 0.01, 0.1, 0.075])
bcal = Button(axcal, 'Calcular')
bcla1 = Button(axcla1, 'Clase1')
bcla2 = Button(axcla2, 'Clase2')

def cla1(event):
    ax.scatter(cordx,cordy, marker='^', c='r')
    plt.draw()
    size_r = len(cordx)
    bcla1 = [0]*size_r
    global total_size
    global ref
    total_size += size_r;
    ref = np.column_stack((cordx,cordy,bcla1))
    del cordx[:]
    del cordy[:]
bcla1.on_clicked(cla1)

def cla2(event):
    ax.scatter(cordx,cordy, marker='o', c='b')
    plt.draw()
    size_r = len(cordx)
    bcla2 = [1]*size_r
    global total_size
    global ref
    total_size += size_r;
    nref = np.column_stack((cordx,cordy,bcla2))
    fref = np.concatenate((ref,nref),axis=0)
    ref = fref
    del cordx[:]
    del cordy[:]
bcla2.on_clicked(cla2)

def cal(event):
    #### Perceptron
	i = 0
	j = 0
	l_rate = 0.3
	counter = 0
	Fx = np.arange(-5,5)

	# initial values
	W1= 2.1
	W2 = 1.2
	W0 = 6.3

	Net = 0.0
	Error = 0.0
	f = 0.0
	X1 = 0
	X2 = 0
	global total_size
	total_size = total_size -1;
	error_count= 0
	while (1) :
	    Net = 0
	    Error = 0
	    #Feature vectors (references)
	    X1 = ref[i][0]
	    X2 = ref[i][1]
	    Y  = ref[i][2]

	    #Weights
	    Net = (X1*W1) + (X2*W2) + (W0)
        # Sigmoid
	    f = 1/(1 + math.exp(-Net))
	    # Error = desired - obtained
	    Error = Y - f;

	    # Adjusting weights
	    if ( (Error >= 0.009) or (-0.009 >= Error)):
	        W1 += l_rate*(Error*(1-f)*f*X1)
	        W2 += l_rate*(Error*(1-f)*f*X2)
	        W0 += l_rate*(Error*(1-f)*f)
	        j += 1
	    else:
	        if ((i ==total_size) and (j == 0)):
	            break
	    if (i == total_size):
	    	i = 0
	    	j = 0
	    else:
	    	i += 1
	    if counter == 10000:
	    	print ("This is the error %f" % Error)
	    	counter = 0
	    counter += 1

	Fy = []
	for ix in Fx:
		Fy.append((-W0-(W1*ix))/W2)
	ax.plot(Fx,Fy)
	plt.draw()

	fig.canvas.mpl_disconnect(cid)

bcal.on_clicked(cal)



def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print ('x = %d, y = %d'%(ix, iy))

    global cordx
    cordy.append(iy)
    cordx.append(ix)

    return onclick

cid = fig.canvas.mpl_connect('key_press_event', onclick)
plt.show()
