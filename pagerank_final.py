# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:04:58 2018

@author: shipratg3
"""

def page_rank(data):
    import pandas as pd
    import numpy as np
    import networkx as nx
    df = pd.DataFrame(data)
    graph=nx.DiGraph()
    h=nx.path_graph(pd.Series.count(np.unique(df[0])))
    graph.add_nodes_from(h)
    graph.add_node(h)
    for i in range(len(df[0])):
        graph.add_edge(df[0][i],df[1][i])
        graph[df[0][i]][df[1][i]]['weight'] = df[3][i]   
    transition_matrix=nx.google_matrix(graph)
    n=min(transition_matrix.shape)
    p0=np.repeat(1/n,n)
    pi=np.matmul(p0,transition_matrix)
    eps=0.0000025
    i=1
    while np.sum(np.abs(pi-p0))>=eps:
        p0=pi
        pi=np.matmul(pi,transition_matrix)
        print(i)
        print(pi)
        i=i+1
    print('The final rank is :',pi)
    
