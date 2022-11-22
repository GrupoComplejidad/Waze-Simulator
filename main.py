import pandas as pd
import numpy as np
import networkx as nx
from datetime import datetime
from pytz import timezone
import pytz
import random

def Init():
    #leemos el dataset
    #Solamente para prueba indicamos el numero de filas q leera
    df=pd.read_csv('Lima-intersecciones_v2.csv', sep=",",encoding = "ISO-8859-1", nrows=1000)
    #Creamos el grafo
    GRAPH = nx.from_pandas_edgelist(df,source='ID_Origen_intereccion',target='ID_Final_Interseccion',edge_attr=['distancia_Km','ID_Final_Interseccion', 'ID_Origen_intereccion','Nombre_Calle','Costo2', 'Latitud_Origen_Interseccion','Longitud_Origen_Interseccion','Latitud_Destino_Interseccion','Longitud_Destino_Interseccion'])
    return GRAPH


def drawGraph(GRAPH):
    pos=nx.spring_layout(GRAPH)
    nx.draw_networkx_nodes(GRAPH, pos, node_size=500)
    nx.draw_networkx_edges(GRAPH, pos, edgelist=GRAPH.edges(), edge_color='black')
    nx.draw_networkx_labels(GRAPH,pos)

def getTime():
    location=pytz.timezone('America/Bogota')
    date=datetime.now(location).hour
    return date


def gettraffic(date):
    factor=1
    if((date>7 and date<9)or(date>18 and date>21)):
        factor=2
    return factor



def getCosto(distancia, factor):
    costo=distancia*1000*factor
    return costo


def update_weights_egde(graph):
    for e in graph.edges():

        r=random.randint(1,100)
        if(r%2==0):
            graph[e[0]][e[1]]['Costo2']=getCosto(graph[e[0]][e[1]]['distancia_Km'], (gettraffic(getTime())))



def clear_weights(graph):
    for e in graph.edges():
        graph[e[0]][e[1]]['Costo2']=graph[e[0]][e[1]]['distancia_Km']
