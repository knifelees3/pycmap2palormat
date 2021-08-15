import struct
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def save_files(val_cho,cmap_name):
    if val_cho==1:
        cmap_fun=cm.get_cmap(cmap_name,256)
        cmap_use=cmap_fun(np.linspace(0,1,256))
        cmap_save=cmap_use[:,0:3]
        file_name='MATLABColormap_'+cmap_name+'_exportedfromPython.txt'
        np.savetxt(file_name,cmap_save)
        print('Colormap files for MATLAB has been generated! ')
    if val_cho==2:
        cmap_fun=cm.get_cmap(cmap_name,256)
        cmap_use=np.array((cmap_fun(np.linspace(0,1,256))*255),int)
        cmap_use[:,-1]=0
        #
        depth=cmap_use.shape[0]
        hlen=24;                            # Header length
        flen=hlen+(4*depth)
        # make file
        filename='OriginColormap_'+cmap_name+'_exportedfromPython.pal'
        newFile = open(filename, "wb")
        # write to file
        # newFile.write(newFileBytes)
        tmp=b'RIFF'
        newFile.write(struct.pack('4B', *b'RIFF'))
        newFile.write(struct.pack('1I', flen-8))
        newFile.write(struct.pack('4B', *b'PAL '))
        newFile.write(struct.pack('4B', *b'data'))
        newFile.write(struct.pack('1I', flen-20))
        newFile.write(struct.pack('2B', 0,3))
        newFile.write(struct.pack('H', depth))
        for num in cmap_use:
            newFile.write(struct.pack('4B', num[0], num[1], num[2], num[3]))
        newFile.close()
        print('Colormap files for Origin has been generated! ')

#var_cho=1: MATLAB
#var_cho=2: Origin

var_cho=2
cmap_name='jet'
save_files(1,cmap_name)