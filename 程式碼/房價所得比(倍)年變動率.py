# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:07:36 2021

@author: ASUS
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('C:/Users/ASUS/21號張德昱python/各縣市房價比.csv', encoding='utf-8')
print(df.to_string())
df.info()
house = df.drop("Unnamed: 0", axis='columns')

data = np.array(house)
fig = plt.figure()
plt.plot(data[:, 0], data[:, 6], '-*', color='green')
for a, b in zip([x for x in data[:, 0]], data[:, 6]):
    plt.text(a, b+0.02, b, ha='center', va='bottom', fontsize=12)
plt.xticks(data[:, 0], rotation='vertical')
plt.title('房價所得比(倍)年變動綠')
plt.xlabel('縣市')
#fig.savefig('房價所得比(倍)年變動值.png', dpi=fig.dpi, bbox_inches='tight')
plt.show()
