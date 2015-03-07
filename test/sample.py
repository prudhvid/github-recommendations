import MySQLdb as mdb
from igraph import *

db = mdb.connect('localhost', 'root', 'pass', 'github');
cursor = db.cursor()


cursor.execute("Select * from org_mem group by user_id")


rows=cursor.fetchall()

cursor.execute("Select * from org_mem group by org_id")
orgs=cursor.fetchall()
print 'yeah1'
result={}
i=0
g=Graph()
g.add_vertices(len(rows))

g.vs["name"]=[int(row[1]) for row in rows]

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
            m1=members[i]
            m2=members[j]
            v1=user_dic[members[i][1]]
            v2=user_dic[members[j][1]]
            print org,v1,v2
            g.add_edge(v1,v2)
            ec+=1
            if ec>1000:
                break
        if ec>1000:
                break
    if ec>1000:
                break
    print 'ec=',ec

#
#
# #make graph from the result dictionary
# # g=Graph()
# # g.add_vertices(result.keys())
summary(g)
# for x in (g.vs):
#     print x;
#

# g.add_edges([(g.vs.select(name=int(row[0]))[0],g.vs.select(name=int(row[1]))[0]) for row in rows ])
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


# g.write_adjacency("user user org.adj")
print 'hey'
# g.write_svg("user user org.svg")
print 'hey2'
