# coding: utf-8

# enregistre tous les noeuds, apex et Ltot dans le fichier nodes
# si le temps existe, il est ajouté en derniere colonne de nodes
# modifer les parametres et exectuer avec:
# python3 get_all_nodes.py

import comptage_noeuds as cn
import read_time
import os
import numpy as np
import sys

def PARAMS():
    path = '/home/hyphes/Clara/2022_11_03_P_S_LEDp/VST/'
    path_s =  '/outputData/'
    s_name = "all_nodes"
    file_time = '/home/hyphes/Clara/2022_11_03_P_S_LEDp/log.txt'
    return path, path_s, s_name, file_time


def get_nodes( path, path_s, s_name):

    allfiles = os.listdir(path)
    files = [ fname for fname in allfiles if fname.endswith('.gpickle')]
    #print files

    nodes = np.zeros( (len(files), 4))

    for inc in range(len(files)):
#    print(files[inc])
        apex, embranchements, Ltot = cn.comptage_noeuds( path, files[inc])
        nodes[inc,1] = apex
        nodes[inc,2] = embranchements
        nodes[inc,3] = Ltot
        temp = files[inc]
        nodes[inc,0] = np.uint8( temp[ str.find(temp,'Movie_') + 6 : str.find(temp,'_gr') ] )

#    nodes[inc,0] = files[inc][16:-20]

    ordre = np.argsort( nodes[:,0])
    nodes[:,0] = nodes[ordre,0]
    nodes[:,1] = nodes[ordre,1]
    nodes[:,2] = nodes[ordre,2]
    nodes[:,3] = nodes[ordre,3]
    return nodes

def read_time( file):

    from datetime import datetime
    import numpy as np
    import sys

    f = np.genfromtxt( file, skip_header=14, dtype=str)

    time = np.zeros(np.shape(f)[0])
    for inc in range( 0, np.shape(f)[0]-1):
#    a[inc] = datetime.strptime(tt[2,1],"%Y-%m-%d")
        temp = datetime.strptime( f[inc+1,2], "%H:%M:%S.%f") - datetime.strptime( f[inc,2], "%H:%M:%S.%f")
        time[inc+1] = temp.seconds

    time = np.cumsum( time)

    return time
    


if __name__ == "__main__":

    path, path_s, s_name, file_time = PARAMS()
    nodes = get_nodes( path, path_s, s_name)

    if os.path.isfile( file_time):
        time = read_time( file_time)
        temp = np.zeros((nodes.shape[0],nodes.shape[1]+1))
        temp[:,:-1] = nodes
        temp[:,-1]  = time[:nodes.shape[0]]
        nodes       = temp
    else:
        print(' ====> NO TIME FILE FOUND <=====')

    if not os.path.exists(path + path_s):
        os.makedirs(path + path_s)

    np.savetxt( path + path_s + s_name + '.txt', nodes )



