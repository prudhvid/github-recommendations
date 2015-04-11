__author__ = '12CS10037'
import  networkx as nx;
import graphlab as gl
import sqlite3
import sys


proj_members=nx.read_pajek('../net_files/project_members.net')


users=[]
projects=[]



for node in proj_members.nodes():
    if node[0]=='u':
        p=proj_members.neighbors(node)
        users+=[node]*len(p)
        projects+=p


data=gl.SFrame({
    'user_id':users,
    'item_id':projects
                })

m = gl.item_similarity_recommender.create(data)
nn = m.get_similar_items()
m2 = gl.item_similarity_recommender.create(data, nearest_items=nn,similarity_type='pearson')

results=m2.recommend()
results.save('results_proj_item.csv',format='csv');
