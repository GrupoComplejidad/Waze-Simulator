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
    
     def clear(self):
        self.input_node_origin.delete(0, last=tkinter.END)
        self.input_node_destine.delete(0, last=tkinter.END)
        self.map_widget.delete(self.input_node_destine)
        self.map_widget.delete(self.input_node_origin)
        clear_weights(self.graph)


        #for e in Init().edges():
        #    marker=self.map_widget.set_marker(float(Init()[e[0]][e[1]]['Latitud_Origen_Interseccion']), float(Init()[e[0]][e[1]]['Longitud_Origen_Interseccion']), text=str(Init()[e[0]][e[1]]['ID_Origen_intereccion']) )

    
    def on_closing(self, event=0):
        self.destroy()
        exit()

    def start(self):
        self.mainloop()



    if __name__ == "__main__":
    app = App()
    app.start()
