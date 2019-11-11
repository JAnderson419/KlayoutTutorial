import os
import klayout.db as pya
import examplePCell

'''
Now that we understand the basics of drawing shapes into a cell, lets create a PCell
that can be called interactively inside klayout. If you have used the macro editor in
Klayout, you know that PCells are stored in lym/py files and are registered with a 
Library so that they can be called from within the application. 

The example in this tutorial is broken into two files. The first is the file that you
are now in, which contains code to generate a test layout for verification while coding
the device geometry.

The second file is "examplePCell.py", which is the file that contains the device
geometry itself as well as the function that registers a PCell library. Once the device 
is coded and verified working without errors, this file can be imported directly into
KLayout to register your PCells for drag and drop placement. Alternatively, you could 
use an approach similar to that in this file to instance cells in the layout from code,
generating a layout entirely in Python.

'''

path = os.path.dirname(os.path.abspath(__file__))
lib = examplePCell.NNO_PCell_Lib()
layout = pya.Layout()
cell1 = layout.add_pcell_variant(lib, 0, {})
# cell1 = layout.add_pcell_variant(lib, 0,
#         {"ito": pya.LayerInfo(1, 0, "ITO Opening 1/0"),
#         "nno": pya.LayerInfo(2, 0, "NNO Pad 2/0"),
#         "fox": pya.LayerInfo(3, 0, "Field Oxide 3/0"),
#         "hfoetch": pya.LayerInfo(4, 0, "HfO2 Etch 4/0"),
#         "w": 40})
layout.convert_cell_to_static(cell1)
layout.write(os.path.join(path, 'test.gds'))