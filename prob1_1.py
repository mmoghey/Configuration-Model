import snap
import numpy as np

USPG = snap.LoadEdgeList(snap.PUNGraph, 'C:\Users\manas\Documents\eBooks\Advanced Databases\HomeWork3\download-20180403T233418Z-001\download\USpowergrid_n4941.txt',0, 1)

k = []
for count in range(1, USPG.GetNodes() + 1):
    N = USPG.GetNI(count)
    k.append(N.GetDeg())


v = []
nid = 1
count = 0
for deg in k:
    for i in range (1, deg+1):
        v.append(nid)
        count = count + 1
    nid = nid + 1

#print len(v), count

v = np.array(v)
cf = []
for i in range (100	):
    G1 = snap.TUNGraph.New()
    while (1):
        v_ran = np.random.permutation(v)
        G1 = snap.TUNGraph.New()
        i = 0
        while (i < len(v_ran)):
            #print i, v_ran[i], i+1, v_ran[i+1]
            if (G1.IsEdge(v_ran[i], v_ran[i+1])):
                break
            if (G1.IsNode(v_ran[i]) == False):
                G1.AddNode(v_ran[i])
            if (G1.IsNode(v_ran[i+1]) == False):
                G1.AddNode(v_ran[i+1])
            G1.AddEdge(v_ran[i], v_ran[i+1])
            #print ("increment i")
            i = i+2
        if ( i == len(v_ran)):
            break
    cf.append (snap.GetClustCf(G1, -1))
avg_cf = sum(cf) / float(len(cf))
print ("##############Problem 1.1###################")
print ("Average clustering coefficient:" , avg_cf)

    





