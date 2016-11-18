import sys
import numpy as np
from PyQt4.QtGui import QIntValidator, QDoubleValidator, QApplication, QSizePolicy
from PyMca5.PyMcaIO import specfilewrapper as specfile
from orangewidget import gui
from orangewidget.settings import Setting
from oasys.widgets import widget

# try:
#     from orangecontrib.xoppy.util.xoppy_calc import xoppy_doc
# except ImportError:
#     print("Error importing: xoppy_doc")
#     raise

# try:
#     from orangecontrib.xoppy.util.xoppy_calc import xoppy_calc_functions1D
# except ImportError:
#     print("compute pressed.")
#     print("Error importing: xoppy_calc_functions1D")
#     raise

class OWfunctions1D(widget.OWWidget):
    name = "functions1D"
    id = "orange.widgets.datafunctions1D"
    description = "xoppy application to compute..."
    icon = "icons/xoppy_functions1D.png"
    author = "create_widget.py"
    maintainer_email = "srio@esrf.eu"
    priority = 10
    category = ""
    keywords = ["xoppy", "functions1D"]
    outputs = [{"name": "xoppy_data",
                "type": np.ndarray,
                "doc": ""},
               {"name": "xoppy_specfile",
                "type": str,
                "doc": ""}]

    #inputs = [{"name": "Name",
    #           "type": type,
    #           "handler": None,
    #           "doc": ""}]

    want_main_area = False

    FROM = Setting(-100.0)
    TO = Setting(100.0)
    NPOINTS = Setting(500)
    FUNCTION_NAME = Setting(0)
    CUSTOM = Setting("sin(x)")
    DUMP_TO_FILE = Setting(1)
    FILE_NAME = Setting("tmp.dat")


    def __init__(self):
        super().__init__()

        box0 = gui.widgetBox(self.controlArea, " ",orientation="horizontal") 
        #widget buttons: compute, set defaults, help
        gui.button(box0, self, "Compute", callback=self.compute)
        gui.button(box0, self, "Defaults", callback=self.defaults)
        gui.button(box0, self, "Help", callback=self.help1)
        self.process_showers()
        box = gui.widgetBox(self.controlArea, " ",orientation="vertical") 
        
        
        idx = -1 
        
        #widget index 0 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "FROM",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 1 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "TO",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 2 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "NPOINTS",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 3 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.comboBox(box1, self, "FUNCTION_NAME",
                     label=self.unitLabels()[idx], addSpace=True,
                    items=['sin(x)', 'cos(x)', 'x^2+x+1', 'Custom'],
                    valueType=int, orientation="horizontal")
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 4 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "CUSTOM",
                     label=self.unitLabels()[idx], addSpace=True)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 5 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.comboBox(box1, self, "DUMP_TO_FILE",
                     label=self.unitLabels()[idx], addSpace=True,
                    items=['Yes', 'No'],
                    valueType=int, orientation="horizontal")
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 6 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "FILE_NAME",
                     label=self.unitLabels()[idx], addSpace=True)
        self.show_at(self.unitFlags()[idx], box1) 

        gui.rubber(self.controlArea)

    def unitLabels(self):
         return ['Abscissa from ','Abscissa to','Number of points','Function','Custom expression','Dump to file','File name']


    def unitFlags(self):
         return ['True','True','True','True','True','True','True']


    #def unitNames(self):
    #     return ['FROM','TO','NPOINTS','FUNCTION_NAME','CUSTOM','DUMP_TO_FILE','FILE_NAME']


    def compute(self):
        fileName = xoppy_calc_functions1D(FROM=self.FROM,TO=self.TO,NPOINTS=self.NPOINTS,FUNCTION_NAME=self.FUNCTION_NAME,CUSTOM=self.CUSTOM,DUMP_TO_FILE=self.DUMP_TO_FILE,FILE_NAME=self.FILE_NAME)
        #send specfile

        if fileName == None:
            print("Nothing to send")
        else:
            self.send("xoppy_specfile",fileName)
            sf = specfile.Specfile(fileName)
            if sf.scanno() == 1:
                #load spec file with one scan, # is comment
                print("Loading file:  ",fileName)
                out = np.loadtxt(fileName)
                print("data shape: ",out.shape)
                #get labels
                txt = open(fileName).readlines()
                tmp = [ line.find("#L") for line in txt]
                itmp = np.where(np.array(tmp) != (-1))
                labels = txt[itmp[0]].replace("#L ","").split("  ")
                print("data labels: ",labels)
                self.send("xoppy_data",out)
            else:
                print("File %s contains %d scans. Cannot send it as xoppy_table"%(fileName,sf.scanno()))

    def defaults(self):
         self.resetSettings()
         self.compute()
         return

    def help1(self):
        print("help pressed.")
        xoppy_doc('functions1D')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = OWfunctions1D()
    w.show()
    app.exec()
    w.saveSettings()
