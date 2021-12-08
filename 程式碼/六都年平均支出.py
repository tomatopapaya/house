# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:56:35 2021

@author: ASUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus']=False
df=pd.read_csv('C:/Users/ASUS/Desktop/我的專題報告/年平均支出.csv',encoding='utf-8')
print(df.to_string())
data=np.array(df)
fig=plt.figure(dpi=200)
plt.barh(data[:,0],data[:,1],color='purple')
plt.title('六都年平均支出(戶)')
plt.xlabel('年平均支出(百萬)')
fig.savefig('六都年所得支出圖表.png',dpi=fig.dpi,bbox_inches='tight')
plt.show()