# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:34:22 2017

@author: ibiyt
"""
import networkx as nx
import os

avgL=0
avgC=0
for graphloc in os.listdir('nullModelHeuristic/'):
    graph=nx.read_gpickle('nullModelHeuristic/'+graphloc)
    print(len(list(nx.connected_components(graph))))
    
#avgL/=100
#avgC/=100
#
#print (avgL)
#print(avgC)