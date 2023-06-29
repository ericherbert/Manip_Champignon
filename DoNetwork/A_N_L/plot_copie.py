# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

#path = '/home/hyphes/29_oct/VST/outputData/'
#s_name = 'all_nodes'
#nodes = np.loadtxt( path + s_name + '.txt' )

x2 = np.linspace(0,10,10)
y2 = x2**2

plt.close(11)
plt.figure(11)
plt.subplot(2,1,1)
plt.plot(x2,y2,'sb')
plt.plot(x2,y2*2,'+r')
plt.plot(x2,y2*4,'^r')
plt.xlabel('Time')
plt.ylabel('Apex')

plt.subplot(2,1,2)
plt.semilogy(x2,y2,'sb')
plt.semilogy(x2,y2*2,'+r')
plt.xlabel('Tlsdibus')
plt.ylabel('sd')


#plt.savefig( path + 'out_apex.png' )


plt.show(block=1)
