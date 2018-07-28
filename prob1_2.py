import snap
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import mlab

USPG_new = snap.LoadEdgeList(snap.PUNGraph, 'C:\Users\manas\Documents\eBooks\Advanced Databases\HomeWork3\download-20180403T233418Z-001\download\USpowergrid_n4941.txt',0, 1)
cc =[]

for count in range(1, 10000):
    num = USPG_new.GetEdges()
    r_int = random.randint(1, num)
    
    iter = USPG_new.BegEI()
    for i in range(1, r_int):
        ext = iter.Next()
    a = iter.GetSrcNId()
    b = iter.GetDstNId()
    
    r_ep = random.randint(1,2)
    if (r_ep == 1):
        u, v = a, b
    else:
        u, v = b, a
    r_int = random.randint(1, num)
    iter = USPG_new.BegEI()
    for i in range(1, r_int):
        ext = iter.Next()
    c = iter.GetSrcNId()
    d = iter.GetDstNId()
    
    r_ep = random.randint(1,2)
    if (r_ep == 1):
        w, x = c, d
    else:
        w, x = d, c
    if (u == w or v == x):
        continue
    if (USPG_new.IsEdge(u,w) or USPG_new.IsEdge(v,x)):
        continue
    n = USPG_new.DelEdge(a,b)
    n = USPG_new.DelEdge(c,d)
    n = USPG_new.AddEdge(u,w)
    n = USPG_new.AddEdge(v,x)
    if (count % 100 == 0):
        cc.append(snap.GetClustCf(USPG_new, -1))
 
print cc

Y = cc
X = range(1,100)
plt.xlabel('iterations / 100')
plt.ylabel('clustering coefficients')
plt.title('Problem 1.2')
plt.plot(X,Y)
plt.show()
   
