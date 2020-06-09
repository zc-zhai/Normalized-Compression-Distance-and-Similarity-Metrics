#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:48:17 2019

@author: zc-zhai
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
try:
    import lzma
except ImportError:
    from backports import lzma
#plt.matshow(dataframe.corr())
#plt.show()
groupfiles_root = "/Users/zc-zhai/Desktop/Malware/coursework/g6"
classfiles_root = "/Users/zc-zhai/Desktop/Malware/coursework/fileClasses"
outputpath = '/Users/zc-zhai/Desktop/Malware/coursework/NCD_value.csv'

def getfilelist():
    allfiles = []
    for root,dirs,files in os.walk(groupfiles_root):
        for file in files:
            if "bin" in file:
                allfiles.append (os.path.join(root,file))
                #print(os.path.join(root,file))
    
    for root,dirs,files in os.walk(classfiles_root):
        for file in files:
            if "bin" in file:
                allfiles.append (os.path.join(root,file))
                
    return allfiles

def NCD(file1, file2):
    x = open(file1, 'rb').read()  # file 1 of any type
    y = open(file2, 'rb').read()  # file 2 of the same type as file 1
    x_y = x + y  # the concatenation of files

    x_comp = lzma.compress(x)  # compress file 1
    y_comp = lzma.compress(y)  # compress file 2
    x_y_comp = lzma.compress(x_y)  # compress file concatenated

    p = len(x_y_comp) - min(len(x_comp), len(y_comp))
    q = max(len(x_comp), len(y_comp))
    ncd = float(p) / float(q)
    #print(format(float(p)/float(q), '.4f'))
    return round(ncd,4)

def genlist():
    allfiles = getfilelist()
    matrix = []
    matrix_single = []
    count = 1
    for i in allfiles:
        for j in allfiles:
            ncd = NCD(i,j)
            print count
            count = count + 1
            matrix_single.append(ncd)
        matrix.append(matrix_single)
        matrix_single = []
    return matrix
#print getfilelist()

df = pd.DataFrame(genlist(), columns = range(28)) 
print df 
df.to_csv(outputpath,sep=',',index=True,header=True)
#print df.columns
#print df.corr()

f = plt.figure(figsize=(10, 7))
#plt.matshow(df.corr(), fignum=f.number)
plt.matshow(df, fignum=f.number)
plt.xticks(range(df.shape[1]), df.columns, fontsize=14, rotation=45)
plt.yticks(range(df.shape[1]), df.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=16)
plt.title('Similarity Matrix for Groupfiles and Classfiles', fontsize=20);
plt.show()
