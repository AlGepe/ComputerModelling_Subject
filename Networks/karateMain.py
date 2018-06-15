import networkx as nx
from pylab import *
from matplotlib import pyplot as plt
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
    # print(x)
    f = math.pow(x-0.25, 3)
    # print(f)
    # print('\n')
    return f

def zacharyData():
    data = np.array([[0, 4, 5, 3, 3, 3, 3, 2, 2, 0, 2, 3, 2, 3, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                     [4, 0, 6, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                     [5, 6, 0, 3, 0, 0, 0, 4, 5, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 3, 0],
                     [3, 3, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [3, 0, 0, 0, 0, 0, 5, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [3, 0, 0, 0, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 3],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                     [2, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [3, 5, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4],
                     [0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
                     [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
                     [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 4, 0, 2, 0, 0, 5, 4],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 2, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 0, 0, 0, 0, 0, 0, 7, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2],
                     [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                     [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0, 0, 0, 0, 3, 2],
                     [0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
                     [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 0, 0, 2, 0, 0, 0, 4, 4],
                     [0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 1, 0, 3, 0, 2, 5, 0, 0, 0, 0, 0, 4, 3, 4, 0, 5],
                     [0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 0, 0, 0, 3, 2, 4, 0, 0, 2, 1, 1, 0, 3, 4, 0, 0, 2, 4, 2, 2, 3, 4, 5, 0]])
    print(data)
    oneMax = np.amax(data)
    thaMax = np.amax(oneMax)
    return data/thaMax

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
        # print(node)
        theSum = 0
        for neighbour in g.neighbors(node):
            oneEdge = (node, neighbour)
            theSum += (g.node[neighbour]['state'] - g.node[node]['state']) * g.edges()[oneEdge]['weight']
        valuesList[node] = (g.node[node]['state'] + D * dt * theSum)
    valuesList[0] = 1.
    valuesList[-1] = .0
    valuesList = abs((valuesList-min(valuesList)) / float(abs(max(valuesList)-min(valuesList))))
    valuesDict = {}
    valuesList[0] = 1.
    valuesList[-1] = .0
    for node in g.nodes():
        valuesDict[node] = {'state' : valuesList[node]}

    nx.set_node_attributes(newG, valuesDict)
    # Update Weights
    valuesList = np.zeros(len(g.edges()))
    j = 0
    for i in g.edges():
        w_i = g.edges()[i]['weight']
        f_value = f(abs(g.node[i[0]]['state'] - g.node[i[1]]['state']))
        valuesList[j] = w_i- beta*w_i*(1-w_i)*dt  * f_value
        newG.edges()[i]['weight'] = w_i- beta*w_i*(1-w_i)*dt  * f_value
        j += 1

    return newG

def stdInitCond(g):
    nx.set_node_attributes(g, 0.5, 'state')
    nx.set_edge_attributes(g, 0.5, 'weight')
    g.node[0]['state'] = 1.
    g.node[len(g)-1]['state'] = .0
    return g

def zacharyCondt(g):
    data = zacharyData()
    print(data)
    nx.set_node_attributes(g, 0.5, 'state')
    nx.set_edge_attributes(g, 0.5, 'weight')
    g.node[0]['state'] = 1.
    g.node[len(g)-1]['state'] = .0
    dictEdges= {}
    for i in range(len(data)):
        for j in range(i, len(data[0])):
            dictEdges[(i, j)] = {'weight' : data[i, j]}
    nx.set_edge_attributes(g, dictEdges)
    return g





g = nx.karate_club_graph()
# g = zacharyCondt(g)
g = stdInitCond(g)
# print(g.node[0])
# print(g.node[33])


# /Initialise
    # /Nodes -> club .5 for all but leaders
    # /Edges -> weight .5 for all     

# Iterations
    # solve ODE for clubs
    # solver ODE for edges
for i in range(5000):
    g = doTimeStep(g, 0.01)
    if not(i%10):
        # print(g.nodes(data=True))
        # print(g.edges(data=True))
        print(i)
        nx.draw_spring(g, cmap = cm.cool, vmin = 0, vmax = 1,
                        with_labels = True,
                        node_color = [g.node[i]['state'] for i in g.nodes()],
                        edge_cmap = cm.binary, edge_vmin = 0, edge_vmax = 1,
                        edge_color = [g[i][j]['weight'] for i, j in g.edges])
        plt.savefig('Std_karate_{0:04d}'.format(i))
        plt.clf()
