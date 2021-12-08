# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:12:12 2021

@author: ASUS
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
df=pd.read_csv('C://Users//ASUS//Desktop//我的專題報告/縣市戶數年增表.csv',encoding='utf-8')
print(df.to_string())
del df['Unnamed: 0'] 
print(df[df["縣市"].isin(["臺北市"])])