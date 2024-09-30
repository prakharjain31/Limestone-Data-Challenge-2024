import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
n = 6
rep = 0
df = pd.read_csv('input_game.csv')
s= set()
# for i in range(180406):
#     row = df.loc[i]
#     s.add(row['p1_id'])
#     s.add(row['p2_id'])
# print(len(s))
# print(s)
#This concludes there are 201 players
l=[]
for x in range(2**n):
    l.append([-1])
t=[]
s=0
for x in range(201):
    t.append(l)
prev = -1
print(t[157][0])
for i in range(180406):
    row = df.loc[i]
    if row['game_id']!=prev:
        s+=1
        prev = row['game_id']
        ff = int(row['p1_id'])
        jj = int(row['p2_id'])
        if row['p1_action']=="TRUST":
            sum1 = 32
        else: 
            sum1 = 0
        if row['p2_action']=="TRUST":
            sum2 = 32
        else: 
            sum2 = 0
        p = 16
        for w in range(5):
            r = df.loc[i+w+1]
            if r['p1_action']=="TRUST":
                sum1 += p
            if r['p2_action']=="TRUST":
                sum2 += p
            p=p/2
        # if t[ff-1][int(sum2)] != -1:
        #     rep += 1
        # if t[jj-1][int(sum1)] != -1:
        #     rep+=1
        ((t[ff-1])[int(sum2)]).append(sum1)
        if ff == 157:
            print(t[ff-1][int(sum2)])
            print(1, int(sum2))
        ((t[jj-1])[int(sum1)]).append(sum2)
        if jj==157:
            print(1, int(sum1))
        
    else:
        continue
print(s)
print(rep)
print(len(t[156][0]))
# for k in range(201):
#     arr = t[k]
#     dict = {}
#     for f in arr:
#         if f == -1:
#             continue
#         else:
#             if f in dict.keys():
#                 dict[f]+=1
#             else:
#                 dict[f]=1
#     sum =0
#     m = 0 
#     maxind = 0
#     for h in dict.keys():
#         sum += dict[h]
#         m = max(m, dict[h])
#         if dict[h]>=m:
#             maxind = h
#     ratio = m/sum
#     if(ratio>0.7):
#         print(h, ratio)
#This is for figuring out maxx
li = [[0 for i in range(201)] for i in range(201)]
for p in range(201):
    for o in range(201):
        if p==o:
            continue
        P = t[p]
        O = t[o]
        for i in range(64):
            if P[i]!=-1 and O[i]!=-1:
                if P[i]==O[i]:
                    li[p][o]+=1
                    li[o][p]+=1
#print(l)
#heat_map = sns.heatmap(l)
#plt.show()
l = [{1}]
correlation_threshold = 11
for i in range(201):
    obj = li[i]
    for j in range(201):
        if j==i:
            continue
        if (obj[j]>correlation_threshold):
            a = False
            for n in l:
                if i in n and j in n:
                    a=True
                if i in n and j not in n:
                    n.add(j)
                    a=True
                if i not in n and j in n:
                    n.add(i)
                    a = True
            if not a:
                l.append({i,j})
# for i in range(201):
#     sum = 0
#     for j in t[i]:
#         if (j!=-1):
#             sum+=1
#     print(sum)
for i in range(1,201):
    li=[]
    b=0
    for k in l:
        if i in k:
            li.append(b)
        b+=1
    if len(li)>0:
        sd=li[0]
        for t in li:
            l[sd].update(l[t])
        for t in range(len(li)):
            ind = len(li)-1-t
            rg = li[ind]
            if sd!=rg:
                l.pop(rg)
# print(l)
# for i in l:
#     print(len(i))