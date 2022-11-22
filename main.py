import pandas as pd
import numpy as np
import networkx as nx
from datetime import datetime
from pytz import timezone
import pytz
import random

#Se lee el dataset "Intersecciones" y se indican los parametros para el grafo, las coordenadas = longitud y latitud 
#asi como la distancia entre ellos
def Init():
    df=pd.read_csv('Intersecciones.csv', sep=",",encoding = "ISO-8859-1", nrows=500)
    GRAPH = nx.from_pandas_edgelist(df,source='ID_Origen_intereccion',target='ID_Final_Interseccion',edge_attr=['distancia_Km','ID_Final_Interseccion', 'ID_Origen_intereccion','Nombre_Calle','Costo2', 'Latitud_Origen_Interseccion','Longitud_Origen_Interseccion','Latitud_Destino_Interseccion','Longitud_Destino_Interseccion'])
    return GRAPH

#Se dibuja el grafo
def draw_Graph(GRAPH):
    pos=nx.spring_layout(GRAPH)
    nx.draw_networkx_nodes(GRAPH, pos, node_size=500)
    nx.draw_networkx_edges(GRAPH, pos, edgelist=GRAPH.edges(), edge_color='black')
    nx.draw_networkx_labels(GRAPH,pos)

#Funcion que nos devuelve la hora, mas especifico con una ubicación, la cual es Lima
def get_Time():
    location=pytz.timezone('America/Lima')
    date=datetime.now(location).hour
    return date

#Como se especifica en el tipo Waze, el trafico a las 11am = 7 am< 11am <2 pm, sera menor por lo cual tiene un valor de 1,menor 
#mientras que si son las 7pm, 5pm < 7pm < 10 pm, presentara un valor mayor de 2
value = 0
def get_Traffic(date):
    global value
    if((date>7 and date<14)):
        value=1
    if((date>17 and date<22)):
        value=2
    return value

#Funcion que nos define el peso
def get_Weight(distance, factor):
    weight=distance*factor
    return weight

#Dado que el peso inicial no es el que esta con el trafico, se ha creado esta funcion para poder modificarlo
#una vez se haya hallado el primer posible recorrido
def update_Weights_egde(graph):
    for e in graph.edges():

        r=random.randint(1,100)
        if(r%2==0):
            graph[e[0]][e[1]]['Costo2']=get_Weight(graph[e[0]][e[1]]['distancia_Km'], (get_Traffic(get_Time())))

#Funcion que nos permite limpiar los pesos, para poder realizar una nueva consulta
def clear_weights(graph):
    for e in graph.edges():
        graph[e[0]][e[1]]['Costo2']=graph[e[0]][e[1]]['distancia_Km']
