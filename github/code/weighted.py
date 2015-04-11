__author__ = 'prudhvi'

import MySQLdb as mdb
import networkx as nx
#import matplotlib.pyplot as plt
#import operator


db = mdb.connect('localhost', '12CS10037', 'btech12', '12CS10037');
cursor = db.cursor()

print 'querying'
cursor.execute("select p1.repo_id,p2.repo_id,count(*) from hproject_members as p1,hproject_members as p2 where p1.user_id=p2.user_id and"
               " p1.repo_id!=p2.repo_id group by p1.repo_id,p2.repo_id");

print 'query returned... making graph'
edges=cursor.fetchall()

g=nx.Graph()

for edge in edges:
    g.add_edge(edge[0],edge[1],weight=int(edge[2]))


nx.write_pajek(g,"sample.net")
