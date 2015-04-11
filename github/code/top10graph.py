__author__ = 'prudhvi'

# import MySQLdb as mdb
import networkx as nx
from networkx.algorithms import bipartite






g=nx.Graph()
print 'reading'
g=nx.read_pajek('net_files/watchers.net')
g2=nx.read_pajek('top50_proj_watcher.net')
print 'reading over'

allp=g2.nodes()
i=0
projects=[]
# subgraph=nx.Graph()
for node in allp:
    if i>50:
        break
    projects.append(node)
    i=i+1

users=[]

for node in projects:
    users+=g.neighbors(node)

subgraph=nx.subgraph(g,users+projects)

g2=nx.Graph()

g2.add_nodes_from(projects)

nx.write_pajek(g2,'top10_proj_watcher.net')

g2=nx.Graph()

g2.add_nodes_from(users)

nx.write_pajek(g2,'top10_user_watcher.net')

nx.write_pajek(subgraph,'top10graph.net')