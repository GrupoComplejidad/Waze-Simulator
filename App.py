import sys
import tkinter
import tkinter.messagebox
from matplotlib.pyplot import text
from numpy import append
from tkintermapview import TkinterMapView
from main import *

class App(tkinter.Tk):

    APP_NAME = "Waze Simulator.py"
    WIDTH = 800
    HEIGHT = 800
    
    
    def addtrafic(self):
        update_weights_egde(self.graph)
        self.marker_list_box.insert(tkinter.END,"Se agrego el factor de trafico")



    if __name__ == "__main__":
    app = App()
    app.start()
