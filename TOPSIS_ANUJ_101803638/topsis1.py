import pandas as pd
import numpy as np
import sys
import os
import math
from os import path
import copy

def topsis(source1,weight,impact,dest1):
    class myexception(Exception):
          pass
    source=source1
    dest=dest1
    if not (path.exists(source)):
        raise myexception("no such file exists")
    if not source.endswith('.csv'):
        raise myexception("format is not supported")
    df1=pd.read_csv(source1)
    col=df1.shape
    if not col[1]>=3:
        raise myexception("imput file must contain 3 or more columns")
    k=0
    for i in df1.columns:
        k=k+1
        for j in df1.index:
            if k!=1:
                val=isinstance(df1[i][j],int)
                val1=isinstance(df1[i][j],float)
                if not val and not val1:
                    raise myexception("values are not numeric")
    w=[]
    l=weight.split(',')
    for i in l:
        k=0
        for j in i:
            if not j.isnumeric():
                if k>=1 or j!='.':
                    raise myexception("format of weight is not correct")
                else:
                    k=k+1
        w.append(float(i))
    if len(w)!=(col[1]-1):
        raise myexception("no. of weight and no. of columns must be equal")
    im=impact.split(',')
    for i in im:
        if i not in {'+','-'}:
            raise myexception("format of impact is not correct")
    if len(im)!=col[1]-1:
        raise myexception("no. of impact and no. of columns must be equal")
    df=copy.deepcopy(df1)
    df.drop(df.columns[[0]],axis=1,inplace=True)
    a=df.to_numpy()
    b=[]
    n=len(a)
    m=len(a[0])
    for i in range(m): 
        b.append(math.sqrt(sum(a[:,i]*a[:,i])))
    normalised_a=[]
    for i in range(n):
        a1=[]
        for j in range(m):
            a1.append(a[i][j]/b[j]*w[j])
        normalised_a.append(a1)
    normalised_a=np.array(normalised_a)
    # print(normalised_a)
    #to find best and worst values
    maximum=normalised_a.max(axis=0)
    minimum=normalised_a.min(axis=0)
    # print(maximum)
    # print(minimum)
    v_pos=[]
    v_neg=[]
    for i in range(m):
        if im[i] == '-':
            v_pos.append(minimum[i])
            v_neg.append(maximum[i])
        if im[i]=='+':
            v_pos.append(maximum[i])
            v_neg.append(minimum[i])
    # print(v_pos)
    # print(v_neg)
    # vpos_vneg=np.add(v_pos,v_neg)
    s_pos=[]
    s_neg=[]
    for i in range(n):
        temp=0
        temp1=0
        for j in range(m):
            temp+=(normalised_a[i][j]-v_pos[j])**2
            temp1+=(normalised_a[i][j]-v_neg[j])**2
        temp=temp**0.5
        temp1=temp1**0.5
        s_neg.append(temp1)
        s_pos.append(temp)
    # print(s_pos)
    # print(s_neg)
    spos_sneg=np.add(s_pos,s_neg)
    # print(spos_sneg)
    topsis_score=[]
    for i in range(n):
        topsis_score.append(s_neg[i]/spos_sneg[i])
    # print(topsis_score)
    df1['Topsis Score']=topsis_score
    df1["Rank"] = df1["Topsis Score"].rank(ascending=False) 
    # print(df1)
    df1.to_csv(dest1,index=False)

# if __name__=='__main__':
#     class myexception(Exception):
#           pass
#     n=len(sys.argv)
#     if n!=5:
#         raise myexception("enter correct number of arguments")
#     source=sys.argv[1]
#     dest=sys.argv[4]
#     if not (path.exists(source)):
#         raise myexception("no such file exists")
#     if not source.endswith('.csv'):
#         raise myexception("format is not supported")
#     df1=pd.read_csv(source)
#     col=df1.shape
#     if not col[1]>=3:
#         raise myexception("imput file must contain 3 or more columns")
#     k=0
#     for i in df1.columns:
#         k=k+1
#         for j in df1.index:
#             if k!=1:
#                 val=isinstance(df1[i][j],int)
#                 val1=isinstance(df1[i][j],float)
#                 if not val and not val1:
#                     raise myexception("values are not numeric")
#     w=[]
#     l=sys.argv[2].split(',')
#     for i in l:
#         k=0
#         for j in i:
#             if not j.isnumeric():
#                 if k>=1 or j!='.':
#                     raise myexception("format of weight is not correct")
#                 else:
#                     k=k+1
#         w.append(float(i))
#     if len(w)!=(col[1]-1):
#         raise myexception("no. of weight and no. of columns must be equal")
#     im=sys.argv[3].split(',')
#     for i in im:
#         if i not in {'+','-'}:
#             raise myexception("format of impact is not correct")
#     if len(im)!=col[1]-1:
#         raise myexception("no. of impact and no. of columns must be equal")
#     topsis(df1,w,im,dest)
    