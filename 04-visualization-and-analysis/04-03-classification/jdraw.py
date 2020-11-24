from matplotlib import pyplot as plt
import numpy as np
import statistics as stats

class Point():
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x {}, y {}".format(self.x, self.y)

class Rect():
    sw = None
    ne = None
    label = ''
    def __init__(self, sw, ne, label):
        self.sw = sw
        self.ne = ne
        self.label = label

    def __str__(self):
        return "x {}, y {}".format(self.sw, self.ne)
    
    def draw(self, plt):
        plt.vlines(self.ne.x, self.sw.y, self.ne.y, colors='blue', linestyles='solid')
        plt.vlines(self.sw.x, self.sw.y, self.ne.y, colors='blue', linestyles='solid')
        plt.hlines(self.sw.y, self.sw.x, self.ne.x, colors='blue', linestyles='solid')
        plt.hlines(self.ne.y, self.sw.x, self.ne.x, colors='blue', linestyles='solid')
        
        plt.annotate(self.label, xy=(stats.mean([self.sw.x, self.ne.x])-len(self.label)/2, stats.mean([self.sw.y, self.ne.y])))
