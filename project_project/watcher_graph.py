__author__ = 'prudhvi'

import MySQLdb as mdb
import networkx as nx
from networkx.algorithms import bipartite


db = mdb.connect('10.5.18.68', '12CS10037', 'btech12', '12CS10037');
cursor = db.cursor()

cursor.execute("Select distinct user_id from watchers ");
users=cursor.fetchall()
cursor.execute("Select distinct repo_id from watchers")
projects=cursor.fetchall()

cursor.execute("select repo_id,user_id from watchers")
edges=cursor.fetchall()

i=0
userdic,projectdic={},{}

users=['u'+str(u[0]) for u in users]
projects=['p'+str(p[0]) for p in projects]



g=nx.Graph()
g.add_nodes_from(projects,bipartite=0)

print 'added project nodes'

g.add_nodes_from(users,bipartite=1)

print 'added user nodes'


for nodes in edges:
    g.add_edge('p'+str(nodes[0]),'u'+str(nodes[1]))

print 'added edges'

nx.write_pajek(g,"watchers.net")


print 'written successfully'