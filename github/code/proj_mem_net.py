import  networkx as nx;
import graphlab as gl
import sqlite3
import sys

conn=sqlite3.connect('../data/sqlite/project_members.sql.sqlite3.db')
cursor=conn.cursor()

print 'opened database successfully'

cursor.execute("select repo_id,user_id from project_members")
edges=cursor.fetchall()

print 'got edges'


g=nx.Graph()

for nodes in edges:
    g.add_edge('p'+str(nodes[0]),'u'+str(nodes[1]))

print 'added edges'

nx.write_pajek(g,"project_members.net")


print 'written successfully'