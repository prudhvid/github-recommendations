import sys 
import MySQLdb as mdb
import requests 
import networkx as nx;
from networkx import *
import matplotlib.pyplot as plt
from numpy import *
import math


con = mdb.connect('10.5.18.68', '12CS10037', 'btech12','12CS10037');


if __name__ == "__main__":
    with con:
        cur=con.cursor();
        cur.execute("select count(*) from watchers");
        r=cur.fetchone();
        cur.execute("""select cnt as k,count(*)/%s as no_of_users from (select user_id,count(*) as cnt from watchers group by user_id) as t group by cnt order by cnt asc""",(r));
        rows=cur.fetchall();

        #print r[0][0],r[0][1];
        l1=[];
        l2=[];
        for i in range(len(rows)):
            l1.append(rows[i][0]);
            l2.append(rows[i][1]);
        plt.plot(l1,l2,color='red');


        cur.execute("select count(distinct(user_id)) from project_members");
        r=cur.fetchone();
        cur.execute("""select cnt as k,count(*)/%s as no_of_users from (select user_id,count(*) as cnt from project_members group by user_id) as t group by cnt order by cnt asc""",(r));
        rows=cur.fetchall();

        #print r[0][0],r[0][1];
        l1=[];
        l2=[];
        for i in range(len(rows)):
            l1.append(rows[i][0]);
            l2.append(rows[i][1]);


        #x=plotdata.l1;
        #y=plotdata.l2;

        plt.plot(l1,l2,color='blue');
        plt.axis([0,60,0,0.5]);


        plt.show();
