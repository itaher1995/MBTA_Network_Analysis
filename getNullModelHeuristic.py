# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:27:47 2017

@author: ibiyt
"""

import numpy as np
import networkx as nx
import random
currentNullModel=nx.read_gpickle('nullModel0.gpickle')
def euclidean_distance(u,v):
    return np.sqrt((u[0]-v[0])**2+(u[1]-v[1])**2)

def nullModel(graph,n):
    '''
    Develops null models using modified degree randomization. Our modifications currently only have a distance threshold of 0.5
    '''
    graphCopy=graph.copy()
    for t in range(100):
        edges, swap=doSwap(graphCopy)
        while graphCopy.has_edge(swap[0][0],swap[0][1]) or graphCopy.has_edge(swap[1][0],swap[1][1]): 
            edges, swap=doSwap(graphCopy)
        graphCopy.remove_edges_from(edges)
        graphCopy.add_edges_from(swap)
        del edges
        del swap
    nx.write_gpickle(graphCopy,'nullModelHeuristic/nullModel{}.gpickle'.format(n))
    return graphCopy
        
        
def doSwap(graph):
    edges=random.sample(graph.edges(),2)
    g=nx.Graph()
    g.add_edges_from(edges)
    while edges[0]==edges[1] or len(g.nodes())<4 or maxEuclid(edges,graph):
            edges=random.sample(graph.edges(),2)
            g=nx.Graph()
            g.add_edges_from(edges)
    gCopy=nx.double_edge_swap(g)
    swap=list(gCopy.edges())
    return edges, swap
def maxEuclid(e,graph):
    if euclidean_distance(graph.nodes()[e[0][0]]['loc'],graph.nodes()[e[1][0]]['loc'])>=0.03 or euclidean_distance(graph.nodes()[e[0][0]]['loc'],graph.nodes()[e[1][1]]['loc'])>=0.03 or euclidean_distance(graph.nodes()[e[0][1]]['loc'],graph.nodes()[e[1][0]]['loc'])>=0.03 or euclidean_distance(graph.nodes()[e[0][1]]['loc'],graph.nodes()[e[1][1]]['loc'])>=0.03:
        return True
    else:
        return False

def main(graph):
    for i in range(100):
        null=nullModel(graph,i)
        del graph
        graph=null

main(currentNullModel)