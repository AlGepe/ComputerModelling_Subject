import networkx as nx
from pylab import *
import numpy as np

def showNet(g):
    pos = nx.spring_layout(g)
    labels = {}
    for i in range(len(g)):
        labels[i] = i
    nx.draw_networkx_nodes(g, pos, node_size=400)
    nx.draw_networkx_edges(g, pos, node_size=400)
    nx.draw_networkx_labels(g, pos, labels, font_zise=12)
    show()

g = nx.karate_club_graph()
states = {}
for i in range(len(g)):
    #states[i] = np.random.ranf()
    states[i] = .5
nx.set_node_attributes(g, states, 'state')
nx.set_edge_attributes(g, 0.5,'weight')
g.node[0]['state'] = 1
g.node[len(g)-1]['state'] = 0


# /Initialise
    # /Nodes -> club .5 for all but leaders
    # /Edges -> weight .5 for all     

# Iterations
    # solve ODE for clubs
    # solver ODE for edges
nx.draw_spring(g, cmap = cm.cool, vmin = 0, vmax = 1,with_labels = True, node_color = [g.node[i]['state'] for i in g.nodes()], edge_cmap = cm.binary, edge_vmin = 0, edge_vmax = 1,edge_color = [g[i][j]['weight'] for i, j in g.edges])
show()
