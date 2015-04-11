import networkx as nx;
import matplotlib.pyplot as plt

g=nx.Graph();

g=nx.read_pajek("top10graph.net")

top50=nx.read_pajek("top10_user_watcher.net");
top50proj=nx.read_pajek("top10_proj_watcher.net");

P=top50proj.nodes();
print "started.."

def cal_r(a,b):
    l1=g.neighbors(a);
    l2=g.neighbors(b);

    k=len(list(set(l1) & set(l2)))

    ans=(k*1.0)/(len(l1)+len(l2));
    if ans!=0:
        print "ans :" ,ans;

    return ans;



def rvalues(u1,P):
    r=[]
    for i in range(len(u1)):
        for j in range(len(P)):
            a=cal_r(u1[i],P[j]);

            r.append((u1[i],P[j],a))
            #r[u1[i]][P[j]]=a;

    return  r;

def getprolist(u):
    return g.neighbors(u);


users=[];

users=top50.nodes();
r=dict();

print len(users);
for i in range(100):

    prolist=[];
    prolist=getprolist(users[i]);
    print "prolist for user ",users[i],"is  ",len(prolist);
    r[users[i]]=rvalues(prolist,list(set(P) - set(prolist)));

    r[users[i]]=sorted(r[users[i]],key=lambda tup: tup[2],reverse=True)
    #print r[users[i]];
    r[users[i]]=[r[users[i]][x] for x in range(0,len(r[users[i]])/5)]
    print r[users[i]];

    # for x in r[users[i]]:
    #     if(x[2]>0):
        #         print x


print 'writing'
f=open('watcher_recom.txt','w');
for i in range(100):
    for x in r[users[i]]:
            f.write(str(users[i])+" "+str(x[1])+" "+ str(x[2])+'\n')



f.close()
