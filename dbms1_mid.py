import sys 
import MySQLdb as mdb
import requests 
import networkx as nx;
from networkx import *
import matplotlib.pyplot as plt

con = mdb.connect('10.5.18.68', '12CS10037', 'btech12','12CS10037');
g=nx.Graph();



if __name__ == "__main__":
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print "MySQL version: %s" % \
        result.fetch_row()[0]

    