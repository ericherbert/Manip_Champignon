# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

path = '/home/hyphes/Clara/Sabrina/ascoS_M20,5x_2019_03_28/VST/outputData/'
s_name = 'all_nodes'
nodes_a = np.loadtxt( path + s_name + '.txt' )

path = '/home/hyphes/Clara/Sabrina/ascoS_M20,5x_2019_04_18/VST/outputData/'
s_name = 'all_nodes'
nodes_b = np.loadtxt( path + s_name + '.txt' )

path = '/home/hyphes/Clara/2019_11_21_P_S_M20,5x/VST/outputData/'
s_name = 'all_nodes'
nodes_c = np.loadtxt( path + s_name + '.txt' )

xa = np.linspace(0,59109,58)
xb = np.linspace(0,61183,60)


plt.close(11)
plt.figure(11)
plt.semilogy(xa,nodes_a[:,1],'xg', markersize=3)
plt.semilogy(xb,nodes_b[:,1],'og', markersize=3)
plt.semilogy(nodes_c[:,4],nodes_c[:,1],'xr', markersize=3)
plt.xlabel('Time')
plt.ylabel('Apex')
plt.savefig( '/home/hyphes/Clara/Graphes/' + 'out_apex_0,5xSg_0,5xCr.png' )

plt.close(12)
plt.figure(12)
plt.semilogy(xa,nodes_a[:,2],'xg', markersize=3)
plt.semilogy(xb,nodes_b[:,2],'og', markersize=3)
plt.semilogy(nodes_c[:,4],nodes_c[:,2],'xr', markersize=3)
plt.xlabel('Time')
plt.ylabel('Nodes')
plt.savefig( '/home/hyphes/Clara/Graphes/' + 'out_nodes_0,5xSg_0,5xCr.png' )

plt.close(13)
plt.figure(13)
plt.semilogy(xa,nodes_a[:,3],'xg', markersize=3)
plt.semilogy(xb,nodes_b[:,3],'og', markersize=3)
plt.semilogy(nodes_c[:,4],nodes_c[:,3],'xr', markersize=3)
plt.xlabel('Time')
plt.ylabel('Total length')
plt.savefig( '/home/hyphes/Clara/Graphes/' + 'out_total_length_0,5xSg_0,5xCr.png' )



plt.show(block=0)
