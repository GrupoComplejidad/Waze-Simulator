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

    def clear_marker_list(self):
        for marker in self.marker_list:
            self.map_widget.delete(marker)
        
        self.marker_list_box.insert(tkinter.END,"Se elimino el camino")
        self.marker_list.clear()
        self.connect_marker()

    if __name__ == "__main__":
    app = App()
    app.start()
