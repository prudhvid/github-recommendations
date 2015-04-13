from time import time

__author__ = '12CS10037'
import  networkx as nx;
import graphlab
import sqlite3
import sys
import json
import graphlab as gl
# sys.stdout = open('file', 'w')
conn=sqlite3.connect('../data/sqlite/users.sql.sqlite3.db')
conn2=sqlite3.connect('../data/sqlite/projects.sql.sqlite3.db')
#
cursor=conn.cursor()
pcursor=conn2.cursor()
#
#
# cursor.execute("select owner_id,name,language,forked_from from projects where id=5")
#
# r=cursor.fetchone()
# print r[0]

# sf = graphlab.SFrame({'user_id': ["0", "0", "0", "1", "1", "2", "2", "2"],'item_id': ["a", "b", "c", "a", "b", "b", "c", "d"],'rating': [1, 3, 2, 5, 4, 1, 4, 3]})
# m = graphlab.recommender.create(sf, target='rating')
model=gl.load_model('models/final')
print 'loaded model',time()
data=gl.SFrame({
    'user_id':['5'],
    # 'item_id':['10','20']
    })

while True:
    u=raw_input("enter username")
    cursor.execute("select * from users where login='%s'"%(u))
    user=cursor.fetchone()
    print user
    results=model.recommend(k=5,users=[str(user[0])],verbose=True)
    print results
    for p in results['item_id']:
        pcursor.execute("select * from projects where id = %s"%(p[1:]))
        print pcursor.fetchall()
# recs = m.recommend()
# recs.save('recs');