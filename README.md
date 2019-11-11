This repository is intended to walk a new user through programatically 
making layout cells in KLayout using Python. 
Examples are ordered in increasing complexity.

To begin, clone this repository to your machine and create a new venv based on 
cpython 3.6 (version currently used by KLayout), installing packages in requirements.txt.
You will then need to download the libraries from 
https://github.com/KLayout/klayout/wiki/KLayout-Python-Module listed
under the "Using the Python package on Windows" section and add them to your path.

Once that is complete, try running 01-DrawingShapes.py to verify that everything works
correctly. If so, you should be able to open the generated test.gds in KLayout and see
a rectangle drawn.

