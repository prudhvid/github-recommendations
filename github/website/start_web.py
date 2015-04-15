from flask import Flask
import sqlite3

app = Flask(__name__)

context = ('./server.crt','./server.key')

print 'loading model'
import graphlab as gl
model=gl.load_model('../code/models/rfm_rating')
print 'done loading model'
# app.run(host='0.0.0.0', port=8100, ssl_context=context, threaded=True, debug=True)






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

    results=model.recommend(k=5,users=['u'+str(user[0])],verbose=True)
    print results
    ans=''
    for p in results['item_id']:
        pcursor.execute("select * from projects where id = %s"%(p[1:]))
        x=pcursor.fetchone()
        # print x
        ans+='<a href=' +str(x[1]).replace('api.', '').replace('repos/','') +'>'+str(x[3]) +'</a><br>'
        # print ans
    return ans

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
