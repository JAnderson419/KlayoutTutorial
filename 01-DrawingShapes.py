import os
import klayout.db as pya

path = os.path.dirname(os.path.abspath(__file__))
print(path)
layout = pya.Layout()

# create layers to use in our layout. LayerInfo takes layer#, datatype, text label as inputs
ito = pya.LayerInfo(1, 0, "ITO Opening 1/0")
nno = pya.LayerInfo(2, 0, "NNO Pad 2/0")
fox = pya.LayerInfo(3, 0, "Field Oxide 3/0")
hfoetch = pya.LayerInfo(4, 0, "HfO2 Etch 4/0")

# assign layers to layout
for l in [ito, nno, fox, hfoetch]:
    layout.layer(l)

top = layout.create_cell("TOP")
top.shapes(ito.layer).insert(pya.Box([0, 0], [1000,1000]))

layout.write(os.path.join(path, 'test.gds'))