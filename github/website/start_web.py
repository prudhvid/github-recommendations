from flask import Flask
import sqlite3
import flask

app = Flask(__name__)

context = ('./server.crt','./server.key')

print 'loading model'
import graphlab as gl
model_contr=gl.load_model('../code/models/rfm_project_user')
model_data=gl.load_model('../code/models/rfm_rating')
model_watch=gl.load_model('../code/models/watcher_item')
print 'done loading model'
# app.run(host='0.0.0.0', port=8100, ssl_context=context, threaded=True, debug=True)


"""
{
"contribution_recommendations":
[

{
"language":"Unknown",
"description":"for tmp use",
"rank":1
,"forks":1
,"stars":39
,"name":"limingth/tmp"
,"reason":"torvalds/linux"

},..
]
"interest_recommendations":


"""


def getJsonData(results,pcursor):
    rank=0
    ans=[]
    for p in results['item_id']:
        item={}
        rank+=1
        pcursor.execute("select * from projects where id = %s"%(p[1:]))
        """
        id,url,owner_id,name,description,language,created_at,ext_ref_id,forked_from,deleted
        """
        x=pcursor.fetchone()
        item['language']=x[5]
        item['description']=x[4]
        item['name']=str(x[1]).replace('api.', '').replace('repos/','')[19:]
        item['rank']=rank
        item['rating']=results['score'][rank-1]
        ans.append(item)
    return ans

def getProjects(u):
    conn=sqlite3.connect('../data/sqlite/users.sql.sqlite3.db')
    conn2=sqlite3.connect('../data/sqlite/projects.sql.sqlite3.db')
    cursor=conn.cursor()
    pcursor=conn2.cursor()

    cursor.execute("select * from users where login='%s'"%(u))
    user=cursor.fetchone()

    print user
    if not user:
        print 'no username'


    ans=dict()

    results=model_contr.recommend(k=5,users=['u'+str(user[0])],verbose=True)
    resultst=model_watch.recommend(k=5,users=['u'+str(user[0])],verbose=True)
    # resultst=gl.SFrame()
    # resultst.append()
    results=results.append(resultst)
    # results['item_id']+=resultst['item_id']
    # results['user_id']+=resultst['user_id']
    # results['score']+=resultst['score']
    # results['rank']+=resultst['rank']
    #
    ans['contribution_recommendations']=getJsonData(results,pcursor)

    results=model_data.recommend(k=10,users=['u'+str(user[0])],verbose=True)
    ans['interest_recommendations']=getJsonData(results,pcursor)

    print ans
    return flask.jsonify(**ans)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    # frame= model.recommend(k=10,users=['u'+str(username)])
    # # frame=gl.SFrame()
    # # return frame['item_id']
    # ret='  '
    # for r in frame['item_id']:
    #     ret+=str(r)+" "
    # return ret
    return getProjects(username)

@app.route("/ssl")
def ssl():
    return "Hello SSL World"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, ssl_context=context, threaded=True, debug=True)
