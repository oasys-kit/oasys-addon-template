
class MyData1D(object):

    def __init__(self, x, y, title="", xlabel="", ylabel=""):
        self.x = x
        self.y = y
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def set_data(self,x=None,y=None,title=None,xlabel=None,ylabel=None):
        if x is not None: self.x = x
        if y is not None: self.y = y
        if title is not None: self.title = title
        if xlabel is not None: self.xlabel = xlabel
        if ylabel is not None: self.ylabel = ylabel

if __name__ == "__main__":
    import numpy
    x = numpy.array([1,2,3,4,5])
    y = x**2
    tmp = MyData1D(x,y)
    pass
