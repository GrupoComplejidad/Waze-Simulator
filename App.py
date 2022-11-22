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
    

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)


        self.title(self.APP_NAME)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Return>", self.search)

        if sys.platform == "darwin":
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.input_node_destine = tkinter.Entry(self, width=10)
        self.input_node_destine.grid(row=0, column=0, pady=10, padx=10, sticky="we")
        self.input_node_destine.focus()

        self.input_node_origin = tkinter.Entry(self, width=10)
        self.input_node_origin.grid(row=0, column=1, pady=10, padx=10, sticky="we")
        self.input_node_origin.focus()

        self.search_bar_button = tkinter.Button(master=self, width=8, text="Search", command=self.search)
        self.search_bar_button.grid(row=0, column=2, pady=10, padx=10)

        self.search_bar_clear = tkinter.Button(master=self, width=8, text="Clear", command=self.clear)
        self.search_bar_clear.grid(row=0, column=3, pady=10, padx=10)

        self.map_widget = TkinterMapView(width=self.WIDTH, height=600, corner_radius=0)
        self.map_widget.grid(row=1, column=0, columnspan=4, sticky="nsew")

        self.marker_list_box = tkinter.Listbox(self, height=8)
        self.marker_list_box.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        self.listbox_button_frame = tkinter.Frame(master=self)
        self.listbox_button_frame.grid(row=2, column=2, sticky="nsew", columnspan=2)

        self.listbox_button_frame.grid_columnconfigure(0, weight=1)

        self.addtrafic_button = tkinter.Button(master=self.listbox_button_frame, width=20, text="add trafic",
                                                 command=self.addtrafic)
        self.addtrafic_button.grid(row=0, column=0, pady=10, padx=10)

        self.clear_marker_button = tkinter.Button(master=self.listbox_button_frame, width=20, text="clear path",
                                                  command=self.clear_marker_list)
        self.clear_marker_button.grid(row=1, column=0, pady=10, padx=10)

        self.connect_marker_button = tkinter.Button(master=self.listbox_button_frame, width=20, text="connect path",
                                                    command=self.connect_marker)
        self.connect_marker_button.grid(row=2, column=0, pady=10, padx=10)

        ##DEFINOS QUE SIEMPRE MUESTRE EL AREA DE LIMA
        self.map_widget.set_address("LIMA")
        self.map_widget.set_zoom(15)

        self.marker_list = []
        self.marker_path = None
        self.marker_lista=[]
        self.search_marker = None
        self.search_in_progress = False

        self.graph=Init()

        ##ESTO ES LO Q DIBUJA LOS MARCADORES
        for e in self.graph.edges():
            marker=self.map_widget.set_marker(float(self.graph[e[0]][e[1]]['Latitud_Origen_Interseccion']), float(self.graph[e[0]][e[1]]['Longitud_Origen_Interseccion']), text=str(self.graph[e[0]][e[1]]['ID_Origen_intereccion']) )
            self.marker_lista.append(marker)
            self.graph[e[0]][e[1]]['Costo2']=self.graph[e[0]][e[1]]['distancia_Km']
            ##print(type(marker.position[0]))
            
 <<<<<<< feature/addtrafic
    
    def addtrafic(self):
        update_weights_egde(self.graph)
        self.marker_list_box.insert(tkinter.END,"Se agrego el factor de trafico")
=======

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
