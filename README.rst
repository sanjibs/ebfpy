EBF 
====
**EBF (Efficient Binary File Format)*** 


The  EBF library is a collection of software tools to read 
and write EBF format files. ebfpy is a module  for Python 2 and 3.
The full EBF copyright notice, 
including terms governing use, modification, and redistribution, 
is contained in  the files COPYING and COPYRIGHT.


Installation
-------------
To install do the following

pip install --user --upgrade git+https://github.com/sanjibs/ebfpy.git@master

unzip ebfpy-master.zip
cd ebfpy-master
python setup.py install

This will install both the python library and the python script ebftk.
ebftk is a general purpose command line utility to work with ebf files. 
If your computer cannot locate ebftkpy, you can just manually copy the 
ebftk to a location which is in your search path.  

Documentation 
--------------
Detailed documentation is available at
http://ebfformat.sourceforge.net/build/index.html
For quick start do 
>>>import ebf
>>>help(ebf) 

