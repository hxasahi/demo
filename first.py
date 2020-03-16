# -*- coding: cp936 -*-
r = [2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5,3.6]  #2.2-3.6
e = [0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00]
v = []
for i in range(0,len(r)):
    rt = r[i]
    for j in range(0,len(e)):
        et = e[j]
        vt = (1-1/rt)/et
        v.append(vt)
        print vt

print(len(v))

for k in range(0,len(v)):
    minnum = v[0]
    if v[k] < minnum:
        minnum = v[k]

for l in range(0,len(v)):
    maxnum = v[0]
    if v[k] > maxnum:
        maxnum = v[k]
print(minnum)
print(min(v))
print(max(v))
print('中文',max(v))
