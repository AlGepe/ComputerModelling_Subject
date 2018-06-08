import networkx as nx
from pylab import *
import numpy as np
import math

def showNet(g):
    pos = nx.spring_layout(g)
    labels = {}
    for i in range(len(g)):
        labels[i] = i
    nx.draw_networkx_nodes(g, pos, node_size=400)
    nx.draw_networkx_edges(g, pos, node_size=400)
    nx.draw_networkx_labels(g, pos, labels, font_zise=12)
    show()

def f(x):
    print(x)
    f = math.pow(x-0.25, 3)
    print(f)
    print('\n')
    return f


def  doTimeStep(g, dt):
    # c = D * sum(c_rest - c) * w_edge
    newG = g.copy()
    nx.set_node_attributes(newG, 0, 'state')
    nx.set_edge_attributes(newG, 0, 'weight')
    beta = 10
    D = 5
    # Update Nodes
    valuesList = np.zeros(len(g.nodes()), dtype=float)
    for node in g.nodes():
        print(node)
        formula = 0
        for neighbour in g.neighbors(node):
            oneEdge = (node, neighbour)
            formula += (g.node[node]['state'] - g.node[neighbour]['state'])  *\
                        g.edges()[oneEdge]['weight']
        valuesList[node] = (g.node[node]['state'] + D * dt * formula)
    valuesList[0] = 1.
    valuesList[33] = .0
    valuesList = abs((valuesList-min(valuesList)) / float(max(valuesList)))
    valuesDict = {}
    for node in g.nodes():
        valuesDict[node] = {'state' : valuesList[node]}

    nx.set_node_attributes(newG, valuesDict)
    # Update Weights
    valuesList = 0
    for i in g.edges():
        w_i = g.edges()[i]['weight']
        f_value = f(abs(g.node[i[0]]['state'] - g.node[i[1]]['state']))
        newG.edges()[i]['weight'] = w_i- beta*w_i*(1-w_i)*dt  * f_value
        newG.edges()[i]['weight'] = w_i- beta*w_i*(1-w_i)*dt  * f_value

    return newG


g = nx.karate_club_graph()
nx.set_node_attributes(g, 0.5, 'state')
nx.set_edge_attributes(g, 0.5,'weight')
g.node[0]['state'] = 1.
g.node[len(g)-1]['state'] = .0
print(g.node[0])
print(g.node[33])


# /Initialise
    # /Nodes -> club .5 for all but leaders
    # /Edges -> weight .5 for all     

# Iterations
    # solve ODE for clubs
    # solver ODE for edges
for i in range(100):
    g = doTimeStep(g, 0.01)
    if not(i%10):
        print(g.nodes(data=True))
        print(g.edges(data=True))
        nx.draw_spring(g, cmap = cm.cool, vmin = 0, vmax = 1,
                        with_labels = True,
                        node_color = [g.node[i]['state'] for i in g.nodes()],
                        edge_cmap = cm.binary, edge_vmin = 0, edge_vmax = 1,
                        edge_color = [g[i][j]['weight'] for i, j in g.edges])
        show()
