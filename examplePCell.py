# import klayout.lib as pya
import klayout.db as pya
import inspect

class TLM(pya.PCellDeclarationHelper):

    def __init__(self):

        # Important: initialize the super class
        super(TLM, self).__init__()
        #  self.param("lay", self.TypeLayer, "Layer", default = pya.LayerInfo(2, 0))
        self.param("ito", self.TypeLayer, "Conductor Layer",
                   default=pya.LayerInfo(1, 0, "ITO Opening 1/0"))
        self.param("nno", self.TypeLayer, "Pad Layer",
                   default=pya.LayerInfo(2, 0, "NNO Pad 2/0"))
        self.param("fox", self.TypeLayer, "Isolation Layer",
                   default=pya.LayerInfo(3, 0, "Field Oxide 3/0"))
        self.param("hfoetch", self.TypeLayer, "Isolation Layer",
                   default=pya.LayerInfo(4, 0, "HfO2 Etch 4/0"))
        # self.param("l", self.TypeList, "Length (Squares)", default= [2, 5, 10, 20])
        self.param("w", self.TypeDouble, "Width (um)", default=40)
        # declare the parameters
        # i.e. self.param("l", self.TypeLayer, "Layer", default = pya.LayerInfo(1, 0))
        #      self.param("s", self.TypeShape, "", default = pya.DPoint(0, 0))

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "TLM Structure, \nW={}, 2,5,10,20 Squares".format(self.w)

    # def coerce_parameters_impl(self):
    # TODO: use x to access parameter x and set_x to modify it's value

    def produce_impl(self):
        squares = [2, 5, 10, 20]
        width = self.w * 1000
        length = max(squares) * self.w * 1000
        fox_bloat = 40000
        ito_bloat = 10000

        pad = pya.Box(pya.Point(0, 0), pya.Point(80000, 80000))
        self.cell.shapes(self.nno_layer).insert(pad)
        pads = [pad]
        for s in squares:
            length = s * self.w * 1000
            newpad = pad.moved(length + 80000, 0)
            pads.append(newpad)

        fox_extent_box = pya.Box(0, 0, 160000 + max(squares) * self.w * 1000,
                                 80000).enlarge(pya.Point(fox_bloat, fox_bloat))
        fox_box = pya.Polygon(fox_extent_box)
        fox_box_cutout = pya.Region(pya.Box(pya.Point(80000, 40000 - width / 2),
                                            pya.Point(80000 + length,
                                                      40000 + width / 2)))
        for p in pads:
            fox_box_cutout.insert(p)
            self.cell.shapes(self.nno_layer).insert(p)
        fox_box = pya.Region(fox_box) - fox_box_cutout
        self.cell.shapes(self.fox_layer).insert(fox_box)

        ito_extent_box = fox_extent_box.dup()
        ito_extent_box.enlarge(pya.Point(ito_bloat, ito_bloat))
        ito_iso = pya.Polygon(ito_extent_box)
        ito_iso.insert_hole(fox_extent_box)
        self.cell.shapes(self.ito_layer).insert(ito_iso)

        self.cell.shapes(self.hfoetch_layer).insert(ito_extent_box)

    # optional:
    # def can_create_from_shape_impl(self):
    #   TODO: determine if we have a shape that we can use to derive the
    #   PCell parameters from and return true in that case
    #
    # optional:
    # def parameters_from_shape_impl(self):
    #   TODO: change parameters using set_x to reflect the parameter for the
    #   given shape
    #
    # optional:
    def transformation_from_shape_impl(self):
        return pya.Trans(self.shape.bbox().center())
    #   TODO: return a RBA::Trans object for the initial transformation of
    #   the instance

# TODO: add more PCell classes ..

class NNO_PCell_Lib(pya.Library):

    def __init__(self):
        # TODO: change the description
        self.description = "My PCell library"

        # register the PCell declarations
        # TODO: change the names
        self.layout().register_pcell("TLM2", TLM())
        # TODO: register more PCell declarations

        # register our library with the name "PCellLib"
        # TODO: change the library name
        self.register("NNO_PCell_Lib")