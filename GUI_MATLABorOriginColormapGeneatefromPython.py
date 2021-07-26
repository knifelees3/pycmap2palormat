"""
===============
The python files for generating the MATLAB or Origin colormap files.
This program is a python version of the MATLAB function "cmap2pal" on file exchange
===============

"""
# %%
from tkinter import *

from tkinter.ttk import *

import tkinter
import struct
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from matplotlib import cm
import matplotlib.pyplot as plt
#cmap_name='Purples'


window = tkinter.Tk()
# window.geometry('350x400')
window.wm_title("Python colormaps to Origin or MATLAB")



def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)




def _quit():
    window.quit()     # stops mainloop
    window.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def plot():
    cmap_name=str(txt.get())
    fig=Figure(figsize=(5, 4), dpi=100)
    ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(cmap_name))
    ax.set_title( cmap_name, va='center', ha='right', fontsize=15)
    #anvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.draw()
    #canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    #toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    #canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def save_files():
    val_cho=selected.get()
    cmap_name=str(txt.get())
    if val_cho==1:
        cmap_fun=cm.get_cmap(cmap_name,256)
        cmap_use=cmap_fun(np.linspace(0,1,256))
        cmap_save=cmap_use[:,0:3]
        file_name='MATLABColormap_'+cmap_name+'_exportedfromPython.txt'
        np.savetxt(file_name,cmap_save)
        lbl_res.configure(text='Colormap files for MATLAB has been generated! ')
    if val_cho==2:
        cmap_fun=cm.get_cmap(cmap_name,256)
        cmap_use=np.array((cmap_fun(np.linspace(0,1,256))*255),int)
        cmap_use[:,-1]=0
        #
        depth=cmap_use.shape[0]
        hlen=24;							# Header length
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
        lbl_res.configure(text='Colormap files for Origin has been generated! ')



explanation = """Author: Zhaohua Tian
Email: knifelees3@gmail.com
Web: knifelees3@github.io
This program generates the Origin or MATLAB used colormap files from python. You can
 preview the colormaps and then export the corlormap into files with extension of
  '.pal' (Origin format) or '.txt' (MATLAB format), The files are saved on the same
path of the program. 
Posted on: 2021-07-24"""
lbl_1 = Label(window, text=explanation)
lbl_1.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


lbl_cmp = Label(window, text="Type the name of colormaps")
lbl_cmp.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

txt = tkinter.ttk.Entry(window,width=100)
txt.insert(END, 'jet')
txt.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

btn_show = tkinter.Button(master=window, text="Show the colormaps", command=plot)
btn_show.pack(side=tkinter.TOP)






cmap_name=str(txt.get())
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

fig=Figure(figsize=(5, 4), dpi=100)
ax=fig.add_subplot(111)
ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(cmap_name))
#fig.add_subplot(111).plot([1,2,3,4,])
ax.set_title( cmap_name, va='center', ha='right', fontsize=15)

canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
canvas.mpl_connect("key_press_event", on_key_press)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



lbl_choice = Label(window, text="Choose to generate MATLAB or Origin color map files")

lbl_choice.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# combo = tkinter.ttk.Combobox(window)

# combo['values']= ('MATLAB', 'Origin')

# combo.current(1) #set the selected item

# combo.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
selected = IntVar()
rad_MATLAB = Radiobutton(window,text='To MATLAB', value=1,variable=selected)
rad_MATLAB.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
rad_Origin = Radiobutton(window,text='To Origin', value=2,variable=selected)
rad_Origin.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

lbl_gen = Label(window, text="Use the generate button to generate files")
lbl_gen.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

btn_gen = tkinter.Button(master=window, text="Generate", command=save_files)
btn_gen.pack(side=tkinter.TOP)

lbl_res = Label(window, text="Files are not generated yet")
lbl_res.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


tkinter.mainloop()
