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

    def connect_marker(self):
        position_list = []

        for marker in self.marker_list:
            position_list.append(marker.position)

        if self.marker_path is not None:
            self.map_widget.delete(self.marker_path)

        if len(position_list) > 0:
            self.marker_path = self.map_widget.set_path(position_list)

    if __name__ == "__main__":
    app = App()
    app.start()
