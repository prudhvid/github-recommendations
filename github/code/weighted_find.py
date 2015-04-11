__author__ = 'prudhvi'
import snap
import networkx as nx
from multiprocessing import Process

# g=nx.read_pajek("sample.net")
# print g.edges()
print 'loading graph'
g=snap.LoadPajek_PUNGraph('weighted.net')
print 'loaded graph from file.'

def pagerank(g):
    print 'executing pagerank.'
    PRank=snap.TIntFltH()
    snap.GetPageRank_PUNGraph(g,PRank)
    print 'page rank done'
    PRank.SortByDat(False)

    f=open('pagerank.txt','w')
    i=0
    for item in PRank:
        i+=1
        f.write(str(item)+' '+str(PRank[item])+str('\n'))
    f.close()
    print 'writte page rank values to file'

def clusteringcf(g):
    cf=snap.GetClustCf_PUNGraph(g)
    return cf

def pageRank_components(g):
    print 'executing pagerank components ---- getting components for page rank'
    Components=snap.TCnComV()
    snap.GetWccs(g,Components)
    f=open('component_pr.txt','w')
    cgraphs=[]
    for com in Components:
        v=snap.TIntV()
        for ni in com:
            v.Add(ni)
        cgraphs.append(snap.GetSubGraph_PNGraph(g,v))

    print 'components retrived for pagerank'
    f.write('Total components:'+str(len(cgraphs))+'\n')
    for graph in cgraphs:
        if graph.GetNodes()==2:
            continue
        sprank=snap.TIntFltH()
        snap.GetPageRank_PNGraph(graph,sprank)
        sprank.SortByDat(False)
        f.write(str(graph.GetNodes())+' '+str(sprank[sprank.BegI().GetKey()])+'\n')
    f.close()
    print 'finished writing pagerank components values'


def component_distribution(g):
    print 'executing component distribution --- getting components'
    ComponentDist = snap.TIntPrV()
    snap.GetWccSzCnt(g, ComponentDist)
    f=open('component_distribution.txt','w')
    f.write("Size  - Number of Components:\n")
    for comp in ComponentDist:
        f.write("% d \t % d\n" % (comp.GetVal1(), comp.GetVal2()))
    f.close()
    print 'finshed componet distribution'




snap.PrintInfo(g, "Python type PUNGraph", "info-pngraph.txt", False)



# pr=Process(target=pagerank,args=(g,))
# cd=Process(target=component_distribution,args=(g,))
# prc=Process(target=pageRank_components,args=(g,))
#
# pr.start()
# cd.start()
# prc.start()
#
# pr.join()
# cd.join()
# prc.join()
