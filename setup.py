try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(name='ebfpy',
      version='0.0.30',
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
      long_description_content_type="text/x-rst",
      long_description=long_description
)
