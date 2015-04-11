__author__ = 'prudhvi'

import MySQLdb as mdb
import networkx as nx
from networkx.algorithms import bipartite






g=nx.Graph()
print 'reading'
g=nx.read_pajek('net_files/watchers.net')

print 'reading over'

print g.number_of_nodes()

users=[node for node in g.nodes() if node[0]=='u']
# print users

projects=[node for node in g.nodes() if node[0]=='p']
# print projects

user_degree=sorted(nx.degree(g,users).values(),reverse=True)
proj_degree=sorted(nx.degree(g,projects).values(),reverse=True)


uthre=user_degree[len(user_degree)/10]
pthres=proj_degree[len(proj_degree)/40]

# print user_degree
print uthre,pthres

fnuser,fnproj=[],[]

# for x in g.nodes():
#     if(g.degree(x)>=uthre and x[0]=='u'):
#         fnuser.append(x)
#     elif(g.degree(x)>=pthres and x[0]=='p'):
#         fnproj.append(x)

for x in g.nodes():
    if(g.degree(x)>=pthres and x[0]=='p'):
        fnuser+=g.neighbors(x)
        fnproj.append(x)


g2=nx.Graph()

g2.add_nodes_from(fnuser)

nx.write_pajek(g2,'top50_user_watcher.net')

g2=nx.Graph()

g2.add_nodes_from(fnproj)

nx.write_pajek(g2,'top50_proj_watcher.net')



