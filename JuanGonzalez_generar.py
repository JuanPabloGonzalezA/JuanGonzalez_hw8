import numpy as np
import matplotlib.pyplot as plt

def sample_1(N):
	numeros=np.array([-10, -5, 3, 9])
	return np.random.choice(numeros, N, p=[0.1, 0.4, 0.2, 0.3])#devuelve distro aleatoria con las probabilidades indicadas

def sample_2(N):
	return np.random.exponential(0.5,N)#devuelve numeros aleatorios con distro exp con beta = 0.5

def get_mean(sampling_fun,N,M):
	medias=np.zeros(M)#arreglo de medias
	for i in range(M):#recorrido para sacar las m medias
		medias[i]=np.mean(sampling_fun(N))
	return medias

n=np.array([10,100,1000])#arreglo con los distintos valores de n
m=10000#valor de M
medias_1=np.zeros((m,3))#arreglo que guarta las m medias para 3 enes de sample1
medias_2=np.zeros((m,3))#lo de arriba pero con sample 2
texto='sample_'#texto que me da pereza escribir dos veces
for i in range(3):#recorrido para cada n
	medias_1[:,i]=get_mean(sample_1,n[i],m)
	medias_2[:,i]=get_mean(sample_2,n[i],m)
	np.savetxt(texto+'1_'+str(n[i])+'.txt',medias_1[:,i])#archivo con las m medias para cada n
	np.savetxt(texto+'2_'+str(n[i])+'.txt',medias_2[:,i])
