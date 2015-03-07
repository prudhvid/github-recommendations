__author__ = 'prudhvi'

# from igraph import *
import networkx as nx
import matplotlib.pyplot as plt
"""
try:
    g.write_pickle("user user org.pic")
except:
    pass
try:
    g.write_dimacs("user user org.dim")
except:
    pass
try:
    g.write_graphmlz("user user org.gmz")
except:
    pass
try:
    g.write_picklez("user user org.picz")
except:
    pass

g.write_adjacency("user user org.adj")

g.write_svg("user user org.svg")


"""


print('initialising module .. reading graph')
# g=Graph.Read_Pickle("user user org.pic")
# g2=nx.Graph()
# g3=nx.read_gpickle("user user org.pic")
g=nx.read_gpickle("user user org.pic")
# print g2
g=nx.convert_node_labels_to_integers(g)
print 'writing pajek'
# nx.write_pajek(g,"org_mem.net")
nx.write_adjlist(g,"org_mem.adj")
nx.write_yaml(g,"org_mem.yaml")
# plt.show()
# print('reading graph done.. layout graph initilaizing')
# layout = g.layout("")
# print('done.. strting to plot graph')
# plot(g, layout = layout)
# print 'plot done :D'