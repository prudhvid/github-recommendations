__author__ = 'prudhvi'

import MySQLdb as mdb
import  networkx as nx
import matplotlib.pyplot as plt


db = mdb.connect('localhost', 'root', 'pass', 'github');
cursor = db.cursor()


cursor.execute("Select * from org_mem group by user_id")


rows=cursor.fetchall()

cursor.execute("Select * from org_mem group by org_id")
orgs=cursor.fetchall()
print 'yeah1'
result={}
i=0
g=nx.Graph()
# g.add_nodes_from([row[1] for row in rows])



user_dic={}

index=0
for row in rows:
    if not user_dic.has_key(int(row[1])):
        user_dic[int(row[1])]=index
        index=index+1

print 'yeah2'
ec=0

for org in orgs:
    cursor.execute("select * from org_mem where org_id=%s",org[0])
    members=cursor.fetchall()
    for i in range(0,len(members)):
        for j in range(i+1,len(members)):
            g.add_edge(members[i][1],members[j][1])
            ec+=1
            if ec>20000:
                break
        if ec>20000:
                break

        print members[i],ec
    if ec>20000:
        break



#
#
# #make graph from the result dictionary
# # g=Graph()
# # g.add_vertices(result.keys())
print g,'yeah dude!'
g=nx.convert_node_labels_to_integers(g)
print 'conversion done!!'
# try:
#     nx.draw(g)
#     plt.show()
# except:
#     pass
# for x in (g.vs):
#     print x;
#

# g.add_edges([(g.vs.select(name=int(row[0]))[0],g.vs.select(name=int(row[1]))[0]) for row in rows ])
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
