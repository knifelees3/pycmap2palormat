# pycmap2palormat

![image-20210724211211555](C:\Users\knifelee\AppData\Roaming\Typora\typora-user-images\image-20210724211211555.png)

## English 

* The program can do what: 

Export the python's colormap into MATLAB (txt files) or Origin (.pal) format. 

The python [colormaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html) are very comprehensive and beautiful. We may want use it in Origin or MATLAB. This program aims to generate such kind of colormap files .

[](https://matplotlib.org/stable/_images/sphx_glr_colormaps_003.png)

The generated '.pal' files can be used in origin and the 'txt' files can be used in MATLAB.

This is actually a python version of the MATLAB function [cmap2pal](https://www.mathworks.com/matlabcentral/fileexchange/43114-cmap2pal-convert-matlab-colormap-to-binary-pal-format). To write this I got help from the stack overflow:

[How to write char and integer into binary files with specificed precison using python?](https://stackoverflow.com/questions/68506574/how-to-write-char-and-integer-into-binary-files-with-specificed-precison-using-p)

* How to use:

This program has a plain version `MATLABorOriginColormapGeneratefromPython.py` which directly export the colormap files or another version `GUI_MATLABorOriginColormapGeneratefromPython.py` which has a GUI as blew. You could type  the name of the colormaps in python and then preview the colormap in the GUI and finally export the corresponding files.



## 中文

* 程序的用途：

Python的颜色图（ [colormaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html)）非常多而且非常好看，在用Origin或者MATLAB的时候自己也想用Python的颜色图，因此写了这样一个程序，其实已经有一个将MATLAB程序导出为Origin的‘pal’文件的函数[cmap2pal](https://www.mathworks.com/matlabcentral/fileexchange/43114-cmap2pal-convert-matlab-colormap-to-binary-pal-format)，但是我想导出Python的颜色图的话就得先导出一个MATLAB版本的，再将MATLAB导出为‘pal’文件，比较麻烦，因此我‘cmap2pal’做了一点修改，变成了Python版本，并且添加了图像化的界面。具体写的时候一些二进制的输出的问题参见了这个问题的答案：

[How to write char and integer into binary files with specificed precison using python?](https://stackoverflow.com/questions/68506574/how-to-write-char-and-integer-into-binary-files-with-specificed-precison-using-p)

* 如何使用

直接打开程序，选取你要输出的颜色图的名字以及是输出到MATLAB还是Origin格式。

图形化的操作多了一个预览操作，你可以提前预览你输出的颜色图的名字。









