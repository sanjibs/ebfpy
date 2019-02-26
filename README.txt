---------------------------------------------------------------------
EBF (Efficient Binary Format) Software Library and Utilities
Copyright (c) 2012 Sanjib Sharma
All rights reserved.

The  EBF library is a collection of software tools to read 
and write EBF format files. The full EBF copyright notice, 
including terms governing use, modification, and redistribution, 
is contained in  the files COPYING and COPYRIGHT.
--------------------------------------------------------------------

To install do the following

tar -zxvf libebf_python_x.x.x.tar.gz
cd libebf_python_x.x.x
python setup.py install

This will install both the python library and the python script ebftkpy.
ebftkpy is a general purpose command line utility to work with ebf files. 
If your computer cannot locate ebftkpy, you can just manually copy the 
ebftkpy to a location which is in your search path.  
 

Detailed documentation is available in ebfdocs/index.html.
For quick start do 
>>>import ebf
>>>help(ebf) 

