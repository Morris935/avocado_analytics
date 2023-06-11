# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 00:35:07 2022

@author: ADMIN
"""
import pandas as pd

data = pd.read_csv("avocado.csv")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

data.head()
