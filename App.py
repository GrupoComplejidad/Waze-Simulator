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

    def search(self, event=None):

        print(self.input_node_destine.get(), self.input_node_origin.get())
        djk_path=nx.dijkstra_path(self.graph, source=int(self.input_node_destine.get()), target=int(self.input_node_origin.get()), weight='Costo2')
        print(djk_path)
        for p in djk_path:##Probando el cambio de peso
            for e in self.graph.edges():
                if(p==self.graph[e[0]][e[1]]['ID_Origen_intereccion']):
                    print(p,self.graph[e[0]][e[1]]['ID_Origen_intereccion'])
                    marker=self.map_widget.set_marker(float(self.graph[e[0]][e[1]]['Latitud_Origen_Interseccion']), float(self.graph[e[0]][e[1]]['Longitud_Origen_Interseccion']), text=str(self.graph[e[0]][e[1]]['ID_Origen_intereccion']) )
                    self.marker_list.append(marker)
                    self.marker_list_box.insert(tkinter.END, f" {marker.position}. {marker.text} ")

                ##print(type(marker.position[0]))

    if __name__ == "__main__":
    app = App()
    app.start()
