__author__ = '12CS10037'
__author__ = '12CS10037'
import  networkx as nx;
import graphlab as gl

import sqlite3
import sys

conn=sqlite3.connect('../data/sqlite/projects.sql.sqlite3.db')

cursor=conn.cursor()

g=nx.Graph();

g=nx.read_pajek("./watchers.net")
print 'got watchers'
proj_members=nx.read_pajek('./project_members.net')
print 'got data'
# print proj_members.nodes()
users_proj_dic={}
users=[]
projects=[]
rating=[]


cursor.execute("select id,owner_id,name,language,forked_from,description from projects")
projects_data=cursor.fetchall()
projects_dict={}
for p in projects_data:
    projects_dict[p[0]]=p[1:]

print 'got entire data'

for node in g.nodes():
    if node[0]=='u':
        p=g.neighbors(node)

        for tp in p:
            users_proj_dic[(node,tp)]=5


for node in proj_members.nodes():
    if node[0] == 'u':
        p = proj_members.neighbors(node)

        for tp in p:
            key=(node,tp)
            users_proj_dic[key] = users_proj_dic.get(key, 0) + 11
            # cursor.execute("select id,forked_from from projects where id=%s"%(tp[1:]))
            res=projects_dict.get(tp[1:],None)
            if not res or not res[1]:
                continue

            key=(node,'p'+str(res[3]))
            users_proj_dic[key]=users_proj_dic.get(key, 0) + 7


for key,value in users_proj_dic.items():
    users.append(key[0])
    projects.append((key[1]))
    rating.append(value)

print users[0:100]
print projects[0:100]
print rating[0:100]
print len(rating),len(projects),len(users)
data=gl.SFrame({
    'user_id':users,
    'item_id':projects,
    'rating':rating
    })

uprojects=list(set(projects))
upnames=[]
uforked=[]
ulanguage=[]
udescription=[]

rlist=[]

for p in uprojects:
    # cursor.execute("select owner_id,name,language,forked_from,description from projects where id=%s"%(p[1:]))
    # print "select owner_id,name,language,forked_from from projects where id=%s"%(p[1:])
    r=projects_dict.get(p[1:],None)
    if not r:
        rlist.append(p)
        continue
    # print r
    upnames.append(r[1])
    ulanguage.append(r[2])
    if r[3]:
        uforked.append(1)
    else:
        uforked.append(0)
    udescription.append(r[4])

for r in rlist:
    uprojects.remove(r)
print len(uprojects),len(upnames),len(uforked),len(ulanguage)

itemdata=gl.SFrame({
    'item_id':uprojects,
    'name':upnames,
    'language':ulanguage,
    'forked_from':uforked,
    'description':udescription
})

print itemdata
itemdata.save('csv/project_data1',format='binary')
data.save('csv/data1',format='binary')
# model=gl.recommender.factorization_recommender.create(data,target='rating',item_data=itemdata)
# print model
# gl.load_sframe()
# model.save('models/final_large')
# results=model.recommend(k=5)
# # print results
# results.save('results_final.csv',format='csv')




