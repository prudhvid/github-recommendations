__author__ = 'prudhvi'

import MySQLdb as mdb
import networkx as nx
#import matplotlib.pyplot as plt



#db = mdb.connect('10.5.18.68', '12CS10037', 'btech12', '12CS10037');

db = mdb.connect('localhost', '12CS10037', 'btech12', '12CS10037');
cursor = db.cursor()

cursor.execute("Select * from projects where forked_from is not NULL ");

rows=cursor.fetchall()

g=nx.DiGraph()

for row in rows:
    g.add_edge(row[0],row[8])

nx.write_pajek(g,"distribution.net")
# plt.show()
# print g.edges()
#

# degrees=nx.degree_histogram(g)
iter=g.in_degree_iter()

node_number=g.number_of_nodes()
ind_dist={}
try:
    while True:
        deg=iter.next()
        if(ind_dist.has_key(deg[1])):
            ind_dist[deg[1]]+=1
        else:
            ind_dist[deg[1]]=1
except StopIteration:
    pass



distribution=[(key,value*1.0/node_number) for key,value in ind_dist.iteritems()]
# degrees=[degree for degree in degrees if degree>1 ]
# print degrees
f=open('distribution','w')
for dis in distribution:
	f.write(str(dis[0])+' '+str(dis[1])+'\n')

f.close()



"""
sub-component degree distribution
"""

#graphs=nx.connected_component_subgraphs(nx.Graph(g))
