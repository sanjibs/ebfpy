EBF 
====
**EBF (Efficient Binary File Format)*** 


The  EBF library is a collection of software tools to read 
and write EBF format files. ebfpy is a module  for Python 2 and 3.
The full EBF copyright notice, including terms governing use, modification,
and redistribution, is contained in  the files COPYING and COPYRIGHT.


Description
------------
EBF is a binary format for storing data. It is designed to read and write
data, easily and efficiently.

* Store multiple data items in one file, each having a unique tag name
  * tagnames follow the convention of unix style pathname e.g. /x or /mydata/x

* Automatic type and endian conversion  
* Support for multiple programming languages
  * data can easily read in C, C++, Fortran, Java, IDL and Matlab
  * facilitates easy distribution of data
    
* Comprehensive numpy support
  
  * data is read back as numpy arrays
  * almost any numpy array can be written
  * Nested numpy structures are also supported
    
* Read and write directly a recursive dictionary of numpy arrays
* Internally uses hashtable for fast retireival of data items.
  
  * also allows for overwrite prevention


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

