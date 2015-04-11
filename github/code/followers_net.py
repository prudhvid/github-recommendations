import  networkx as nx;
import graphlab as gl
import sqlite3
import sys

conn=sqlite3.connect('../data/sqlite/followers.sql.sqlite3.db')
cursor=conn.cursor()

print 'opened database successfully'

cursor.execute("select follower_id,user_id from followers")
edges=cursor.fetchall()

print 'got edges'


g=nx.Graph()

for nodes in edges:
    g.add_edge(str(nodes[0]),str(nodes[1]))

print 'added edges'

nx.write_pajek(g,"followers.net")


print 'written successfully'