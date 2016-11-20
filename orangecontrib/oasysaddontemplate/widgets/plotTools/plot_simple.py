from PyQt4 import QtGui

from orangecontrib.oasys-addon-template.util.tools import MyData1D

from orangewidget import widget, gui
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class OWPlotSimple(widget.OWWidget):
    name = "oasys-addon-template Data Plot"
    id = "orange.widgets.data.widget_name"
    description = ""
    icon = "icons/plot_simple.png"
    author = ""
    maintainer_email = ""
    priority = 10
    category = ""
    keywords = ["list", "of", "keywords"]
    inputs = [{"name": "oasys-addon-template-data",
                "type": numpy.ndarray,
                "doc": "",
                "handler": "do_plot" }, ]


    def __init__(self):
        super().__init__()
        self.figure_canvas = None

    def do_plot(self, data):
        print(">>plot_simple: data received",data.shape)

        title = None
        xlabel = None
        ylabel = None

        x = data[:,0]
        y = data[:,-1]
        x.shape = -1
        y.shape = -1
        fig = plt.figure()
        plt.plot(x,y,linewidth=1.0, figure=fig)

        if title is not None: plt.title(title)
        if xlabel is not None: plt.xlabel(xlabel)
        if ylabel is not None: plt.ylabel(xlabel)
        plt.grid(True)

        if self.figure_canvas is not None:
            self.mainArea.layout().removeWidget(self.figure_canvas)
        self.figure_canvas = FigureCanvas(fig)
        self.mainArea.layout().addWidget(self.figure_canvas)

def example_1d():
    app = QtGui.QApplication([])
    ow = OWPlotSimple()

    data = numpy.array([
        [  8.47091837e+04,   1.16210756e+12],
        [  8.57285714e+04,   1.10833975e+12],
        [  8.67479592e+04,   1.05700892e+12],
        [  8.77673469e+04,   1.00800805e+12] ])

    ow.do_plot(data)

    ow.show()
    app.exec_()
    ow.saveSettings()

def example_1d_object():
    app = QtGui.QApplication([])
    ow = OWPlotSimple()

    data = numpy.array([
        [  8.47091837e+04,   1.16210756e+12],
        [  8.57285714e+04,   1.10833975e+12],
        [  8.67479592e+04,   1.05700892e+12],
        [  8.77673469e+04,   1.00800805e+12] ])

    tmp = MyData1D(data[0,:],data[1,:],title="test")

    ow.do_plot(tmp)

    ow.show()
    app.exec_()
    ow.saveSettings()


def example_2d_nparray():
    app = QtGui.QApplication([])
    ow = OWPlotSimple()

    x = numpy.linspace(-4, 4, 20)
    y = numpy.linspace(-4, 4, 20)
    z = numpy.sqrt(x[numpy.newaxis, :]**2 + y[:, numpy.newaxis]**2)

    ow.do_plot(z)

    ow.show()
    app.exec_()
    ow.saveSettings()

if __name__ == '__main__':

    example_1d_nparray()
    #example_2d()

