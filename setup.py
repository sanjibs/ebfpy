try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup
setup(name='ebfpy',
      version='0.0.20',
      description='a module to read and write .ebf files (efficient and easy to use binary format) for python 2 and 3 ',
      py_modules=['ebf'],
      scripts=['scripts/ebftk'],	
      author='Sanjib Sharma',
      author_email='bugsanjib@gmail.com',
      platforms=['any'],			
      classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
	"Topic :: Scientific/Engineering"],
      long_description="""\
Python module for reading and writing .ebf files (compatible with Python 3)
---------------------------------------------
EBF is a binary format for storing data. It is designed to   
read and write data, easily and efficiently. 
- Store multiple data items in one file, each having a unique tag name
  + tagnames follow the convention of unix style pathname e.g. /x or /mydata/x
- Automatic type and endian conversion  
- Support for multiple programming languages
  + data can easily read in C, C++, Fortran, Java, IDL and Matlab
  + facilitates easy distribution of data 
- Comprehensive numpy support
  + data is read back as numpy arrays
  + almost any numpy array can be written
  + Nested numpy structures are also supported
- Read and write directly a recursive dictionary of numpy arrays
- Internally uses hashtable for fast retireival of data items. 
  + also allows for overwrite prevention
"""
      )
