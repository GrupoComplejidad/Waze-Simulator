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



    if __name__ == "__main__":
    app = App()
    app.start()
