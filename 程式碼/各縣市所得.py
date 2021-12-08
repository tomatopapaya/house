# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:05:22 2021

@author: ASUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus']=False
df=pd.read_csv('C:/Users/ASUS/Desktop/我的專題報告/各縣市所得.csv',encoding='utf-8')
print(df.to_string())
data=np.array(df)
fig=plt.figure(dpi=200)
plt.barh(data[:,0],data[:,1],color='orange')
plt.title('各縣市所得(戶)')
plt.xlabel('年所得(百萬)')
fig.savefig('各縣市所得圖表.png',dpi=fig.dpi,bbox_inches='tight')
plt.show()