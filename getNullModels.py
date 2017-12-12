# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 02:43:35 2017

@author: ibiyt
"""

import networkx as nx
import numpy as np
from multiprocessing import Pool
import random

G=nx.read_gpickle('MBTA_eff_best.gpickle')

def euclidean_distance(u,v):
    return np.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)

def nullModel(graph,n):
    '''
    Develops null models using modified degree randomization. Our modifications currently only have a distance threshold of 0.5
    '''
    graphCopy=graph.copy()
    for t in range(int(len(graphCopy.edges())*np.log(10**6)/2)):
        edges, swap=doSwap(graphCopy)
        while graphCopy.has_edge(swap[0][0],swap[0][1]) or graphCopy.has_edge(swap[1][0],swap[1][1]): 
            edges, swap=doSwap(graphCopy)
        graphCopy.remove_edges_from(edges)
        graphCopy.add_edges_from(swap)
        del edges
        del swap
    print(nx.is_connected(graphCopy))
    nx.write_gpickle(graphCopy,'nullModels/nullModel{}.gpickle'.format(n))
    del graphCopy
        
        
def doSwap(graph):
    edges=random.sample(graph.edges(),2)
    g=nx.Graph()
    g.add_edges_from(edges)
    while edges[0]==edges[1] or len(g.nodes())<4:
            edges=random.sample(graph.edges(),2)
            g=nx.Graph()
            g.add_edges_from(edges)
    gCopy=nx.double_edge_swap(g)
    swap=list(gCopy.edges())
    return edges, swap

def main():
    for i in range(100):
        nullModel(G,i)

main()