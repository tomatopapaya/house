# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:16:58 2021

@author: ASUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
df=pd.read_csv('C://Users//ASUS//Desktop//我的專題報告/年增量.csv',encoding='utf-8')
print(df.to_string())
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
plt.plot(taipei[:, 0], taipei[:, 2], '-*', color='green')
plt.plot(Xinbei[:, 0],Xinbei[:, 2], '-*', color='yellow')
plt.plot(Taoyuan[:, 0], Taoyuan[:, 2], '-*', color='orange')
plt.plot(Taichung[:, 0], Taichung[:, 2], '-*', color='purple')
plt.plot(Tainan[:, 0], Tainan[:, 2], '-*', color='blue')
plt.plot(Kaohsiung[:, 0],Kaohsiung[:, 2], '-*', color='red')
plt.legend(labels=['臺北市','新北市','桃園市','臺中市','臺南市','高雄市'],loc='center left')

plt.title('六都戶數年度變化',fontsize=14)
plt.xlabel('years',fontsize=10)
plt.ylabel('戶數',fontsize=12)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
fig.savefig('六都戶數年度變化.png', dpi=fig.dpi, bbox_inches='tight')
plt.show()