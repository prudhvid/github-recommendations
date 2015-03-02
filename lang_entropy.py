import sys
import MySQLdb as mdb
import requests
import networkx as nx;
from networkx import *
import matplotlib.pyplot as plt
import math;

con = mdb.connect('10.5.18.68', '12CS10037', 'btech12','12CS10037');

if __name__ == "__main__":
    with con:
        cur=con.cursor();
        cur.execute("select owner_id,language,count(*) from projects group by owner_id limit 3")
        rows1=cur.fetchall()
        cur.execute("select owner_id,language,count(*) from project_new group by owner_id,language limit 10");
        rows2=cur.fetchall();

        """
        entropy_dic={}
        j=0;
        for i in range(len(rows1)):
            val=rows1[i][2];
            id=rows[i][0]
            while(rows2[j][0]==id):
                p=rows[j][2]/val;
                entropy+=p*math.log10(p);
                j=j+1;
            entropy_dic[id]=entropy;
        print entropy_dic;
        """
