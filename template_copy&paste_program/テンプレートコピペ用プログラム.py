'''
アンカーの日付を定義する．
1年間は52週なのでアンカー日付から7を52回足して日付をリストに入れる
テンプレートからコピペして名前を日付[i]_日付[i+1]にする
'''

import datetime
import pandas as pd
import numpy as np
import shutil

name = "髙村将敬"
anchor_date = datetime.date(2023,4,10)
date = [str(anchor_date)]
#dt = anchor_date + datetime.timedelta(days=1)
dt = anchor_date

for i in range(52):
    dt = dt +datetime.timedelta(days=6)
    datestr = str(dt)
    date.append(datestr)
    dt = dt +datetime.timedelta(days=1)
    datestr = str(dt)
    date.append(datestr)
#print(date)

for i in range(52):
    date[i*2] = date[i*2].replace("-" , "")
    date[i*2 + 1] = date[i*2 + 1].replace("2023" , "")
    date[i*2 + 1] = date[i*2 + 1].replace("2024" , "")
    date[i*2 + 1] = date[i*2 + 1].replace("-" , "")
#print(date)

for i in range(52):
    aa = date[i*2] + "-" + date[i*2 +1] + "_" + name + "_" +"週間報告" +".docx"
    shutil.copyfile("週間計画・報告書.docx", aa)
    print(aa)
    
