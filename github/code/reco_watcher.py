__author__ = '12CS10037'
import  networkx as nx;
import graphlab as gl
import sqlite3
import sys



g=nx.Graph();

g=nx.read_pajek("watchers.net")

print 'got data'
users=[]
projects=[]
for node in g.nodes():
    if node[0]=='u':
        p=g.neighbors(node)
        users+=[node]*len(p)
        projects+=p


print len(projects),len(users)
data=gl.SFrame({
    'user_id':users,
    'item_id':projects
                })

model=gl.recommender.item_similarity_recommender.createcreate(data,similarity_type='pearson');

results=model.recommend();
results.save('results_watch_item_based.csv',format='csv');




