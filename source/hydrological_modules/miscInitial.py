# -------------------------------------------------------------------------
# Name:        MiscInitial
# Purpose:
#
# Author:      pb
#
# Created:     13.07.2016
# Copyright:   (c) pb 2016

# -------------------------------------------------------------------------

from management_modules.data_handling import *

class miscInitial(object):

    """
    Miscellaneous repeatedly used expressions
    Definition if cell area comes from regular grid e.g. 5x5km or from irregular lat/lon
    Conversion factors between m3 and mm etc.

    Note:
        Only used in the initial phase.
    """

    def __init__(self, misc_variable):
        self.var = misc_variable

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

    def initial(self):
        """
        - grid area, length definition
        - conversion factors
        - conversion factors for precipitation and pot evaporation
        """

        if checkOption('gridSizeUserDefined'):

            # <lfoption name="gridSizeUserDefined" choice="1" default="0">
            # If option gridsizeUserDefined is activated, users can specify grid size properties
            # in separate maps. This is useful whenever this information cannot be derived from
            # the location attributes of the base maps (e.g. lat/lon systems or non-equal-area
            # projections)
            # Limitation: always assumes square grid cells (not rectangles!). Size of grid cells
            # may vary across map though

            #self.var.cellLengthPcr = loadmap('CellLength',pcr=True)
            #self.var.cellLength = compressArray(self.var.cellLengthPcr)
            # Length of pixel [m]
            # NOT needed only in routing

            # Area of pixel [m2]
            #self.var.cellAreaPcr = loadmap('CellArea',pcr=True)
            #self.var.cellArea = compressArray(self.var.cellAreaPcr)
            self.var.cellArea = loadmap('CellArea')


        else:
            # Default behaviour: grid size is derived from location attributes of
            # base maps. Requirements:
            # - Maps are in some equal-area projection
            # - Length units meters
            # - All grid cells have the same size

            # Length of pixel [m]
            #self.var.PixelLength = celllength()
            # self.var.cellLengthPcr = celllength()
            #self.var.cellLength = maskmapAttr['cell']

            # Area of pixel [m2]
            #self.var.cellAreaPcr = self.var.cellLength ** 2
            self.var.cellArea=np.empty(maskinfo['mapC'])
            self.var.cellArea.fill(self.var.cellLength ** 2)

#            self.var.PixelArea = spatial(self.var.PixelArea)
            # Convert to spatial expresion (otherwise this variable cannnot be
            # used in areatotal function)

# -----------------------------------------------------------------
        # Miscellaneous repeatedly used expressions (as suggested by GF)

        # self.var.InvCellLength = 1.0 / self.var.cellLength
        self.var.InvCellArea = 1.0 / self.var.cellArea
        # Inverse of pixel size [1/m]
        self.var.DtSec = 86400.0
        self.var.DtDay = self.var.DtSec / 86400
        # Time step, expressed as fraction of day (used to convert
        # rate variables that are expressed as a quantity per day to
        # into an amount per time step)
        self.var.InvDtSec = 1 / self.var.DtSec
        # Inverse of time step [1/s]
        self.var.InvDtDay = 1 / self.var.DtDay
        # Inverse of time step [1/d]

       # self.var.DtSecChannel = loadmap('DtSecChannel')
        # Sub time step used for kinematic wave channel routing [seconds]
        # within the model,the smallest out of DtSecChannel and DtSec is used

        self.var.MMtoM = 0.001
        # Multiplier to convert water depths in mm to meters
        self.var.MtoMM = 1000
        # Multiplier to convert water depths in meters to mm
        self.var.MtoM3 = 1.0 * self.var.cellArea
        # Multiplier to convert water depths in m to cubic metres
        self.var.M3toM = 1 / self.var.MtoM3
        # Multiplier to convert from cubic metres to m water slice

        self.var.con_precipitation = loadmap('precipitation_coversion')

        self.var.con_e = loadmap('evaporation_coversion')

        self.var.twothird = 2.0 / 3.0






