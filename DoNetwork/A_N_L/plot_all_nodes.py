# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

path = '/home/hyphes/Clara/2019_11_21_P_S_M20,5x/VST/outputData/'
#path = './VST/outputData/'

s_name = 'all_nodes'

nodes = np.loadtxt( path + s_name + '.txt' )

plt.close(11)
plt.figure(11)
plt.semilogy(nodes[:,4],nodes[:,1],'xb', markersize=3)
plt.xlabel('Time (s)')
plt.ylabel('Apex')
plt.savefig( path + 'out_apex.png' )

plt.close(12)
plt.figure(12)
plt.semilogy(nodes[:,4],nodes[:,2],'oy', markersize=3)
plt.xlabel('Time')
plt.ylabel('Nodes')
plt.savefig( path + 'out_nodes.png' )

plt.close(13)
plt.figure(13)
plt.semilogy(nodes[:,4],nodes[:,3],'^r', markersize=3)
plt.xlabel('Time')
plt.ylabel('Total length')
plt.savefig( path + 'out_total_length.png' )


plt.show(block=0)
