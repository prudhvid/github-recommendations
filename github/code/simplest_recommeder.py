__author__ = '12CS10037'
import  networkx as nx;
import graphlab as gl
import sqlite3
import sys

conn=sqlite3.connect('../data/sqlite/project_members.sql.sqlite3.db')

cursor=conn.cursor()

g=nx.Graph();

g=nx.read_pajek("../net_files/top10graph.net")
proj_members=nx.read_pajek('../net_files/project_members.net')
print 'got data'
print proj_members.nodes()
users=[]
projects=[]
rating=[]
for node in g.nodes():
    if node[0]=='u':
        p=g.neighbors(node)
        users+=[node]*len(p)
        projects+=p
        index=len(rating)
        rating+=[1]*len(p)

        for p1 in p:
            sql='select repo_id from project_members where user_id = %s and repo_id=%s;'%(node[1:],p1[1:])
            print sql
            try:
                cursor.execute(sql)
                cursor.fetchone()
                rating[index]+=2
            except:
                print "Unexpected error:", sys.exc_info()[0]

            index+=1


print len(rating),len(projects),len(users)
data=gl.SFrame({
    'user_id':users,
    'item_id':projects,
    'rating':rating

                })

model=gl.recommender.create(data)
print model

results=model.recommend(k=5)
print results.head()




