# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:51:28 2021

@author: ASUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
df=pd.read_csv('C://Users//ASUS//Desktop//我的專題報告/各年度縣市房價比.csv',encoding='utf-8')
print(df.to_string())
del df['Unnamed: 0'] 
del df['Unnamed: 0.1'] 
print(df[df["縣市"].isin(["臺北市"])])
df1=df[df["縣市"].isin(["臺北市"])]
df2=df[df["縣市"].isin(["桃園市"])]
df3=df[df["縣市"].isin(["臺中市"])]
df4=df[df["縣市"].isin(["臺南市"])]
df5=df[df["縣市"].isin(["高雄市"])]
df6=df[df["縣市"].isin(["新北市"])]
taipei = np.array(df1)
Taoyuan = np.array(df2)
Taichung = np.array(df3)
Tainan = np.array(df4)
Kaohsiung= np.array(df5)
Xinbei=np.array(df6)
fig = plt.figure()
plt.plot(taipei[:, 0], taipei[:, 5], '-*', color='green')
plt.plot(Xinbei[:, 0],Xinbei[:, 5], '-*', color='yellow')
plt.plot(Taoyuan[:, 0], Taoyuan[:, 5], '-*', color='orange')
plt.plot(Taichung[:, 0], Taichung[:, 5], '-*', color='purple')
plt.plot(Tainan[:, 0], Tainan[:, 5], '-*', color='blue')
plt.plot(Kaohsiung[:, 0],Kaohsiung[:, 5], '-*', color='red')
plt.legend(labels=['臺北市','新北市','桃園市','臺中市','臺南市','高雄市'],loc='center left')
for a, b in zip([x for x in taipei[:, 0]], taipei[:, 5]):
    plt.text(a, b+0.1, b, ha='center', va='bottom', fontsize=12)
for a, b in zip([x for x in Taichung[:, 0]],Taichung[:, 5]):
    plt.text(a, b+0.1, b, ha='center', va='bottom', fontsize=12)
for a, b in zip([x for x in Tainan[:, 0]],Tainan[:, 5]):
    plt.text(a, b+0.1, b, ha='center', va='bottom', fontsize=12)
for a, b in zip([x for x in Xinbei[:, 0]],Xinbei[:, 5]):
    plt.text(a, b+0.1, b, ha='center', va='bottom', fontsize=12)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.title('六都房價所得比年度變化',fontsize=14)
plt.xlabel('years',fontsize=10)
plt.ylabel('房價所得比',fontsize=12)
plt.grid()
fig.savefig('六都房價所得比年度變化.png', dpi=fig.dpi, bbox_inches='tight')
plt.show()