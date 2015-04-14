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
# model=gl.load_model('models/watcher_item')

# print 'loaded model',time()

sf=gl.load_sframe('csv/data')
pdata=gl.load_sframe('csv/project_data')
pdata=gl.SFrame(
    {
        'item_id':pdata['item_id'],
        'language':pdata['language'],
        'name':pdata['name'],
        'description':pdata['description']
    }
)
# print sf['user_id']
model=gl.recommender.ranking_factorization_recommender.create(sf,target='rating',item_data=pdata)
model.save('models/pdata_max')
# model=gl.load_model('models/rfm_rating')



while True:
    try:
        u=raw_input("enter username")
        cursor.execute("select * from users where login='%s'"%(u))
        user=cursor.fetchone()
        # print user[0]
        # for row in sf:
        #     count=0;
        #     if row['user_id']=='u'+str(user[0]):
        #         print row
        #         count=count+1
        #         if count<11:
        #             break;


        print user
        if not user:
            print 'no username'
            continue
        results=model.recommend(k=5,users=['u'+str(user[0])],verbose=True)
        print results
        for p in results['item_id']:
            pcursor.execute("select * from projects where id = %s"%(p[1:]))
            x=pcursor.fetchone()
            # print x
            ans=str(x[1]).replace('api.', '').replace('repos/','')
            print ans
    except:
        pass