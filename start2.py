import pymongo
from pymongo import MongoClient
import networkx as nx;
import matplotlib.pyplot as plt

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.local

c=db.followers.find();
g=nx.Graph();

for i in range(0,2000):
	g.add_edge(c[i]['login'],c[i]['follows']);

nx.draw(g)



try:
    nx.write_gpickle(g,"user user org.pic")
except:
    pass
try:
    nx.write_dot(g,"user user org.dot")
except:
    pass
try:
    nx.write_graphml(g,"user user org.graphml")
except:
    pass
try:
    nx.write_gml(g,"user user org.gml")
except:
    pass

nx.write_edgelist(g,"user user org.edges")
nx.write_sparse6(g,"user user org.sprse")
nx.write_adjlist(g,"user user org.adj")
nx.write_pajek(g,"user user org.net")





