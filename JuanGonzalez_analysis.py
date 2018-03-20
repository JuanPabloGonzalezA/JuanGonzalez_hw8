import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opti

pi=np.pi #me da pereza escribir el np siempre entonces mejor pi
def normal_dist(x,mean,sigma):
	return np.sqrt(1.0/(2.0*pi*sigma**2))*np.exp(-1.0*(x-mean)**2/(sigma**2))

def get_fit(filename):
	medias=np.loadtxt(filename)
	y,bins=np.histogram(medias,normed=True)#y freq; bins
	x=(bins[:-1]+bins[1:])*0.5
	popt, pcov = opti.curve_fit(normal_dist,x,y)
	media=popt[0]
	varianza=(popt[1])**2
	plt.hist(medias,normed=True)
	xx=np.linspace(np.min(medias),np.max(medias),100)
	yy=normal_dist(xx,media,np.sqrt(varianza))
	plt.plot(xx,yy)
	plt.savefig(filename[:-4]+".png")
	plt.close()
	print filename+"\tmedia:"+str(media)+"\tvarianza:"+str(varianza) 
n=[10,100,1000]
texto='sample_'
for i in range(3):
	get_fit(texto+'1_'+str(n[i])+".txt")
	get_fit(texto+'2_'+str(n[i])+".txt")
