import pandas as pd

# 讀取CSV文件，跳過第一行，並使用big5編碼
df = pd.read_csv('地震活動彙整_638488919649981406.csv', encoding='big5', skiprows=1)
df = df.drop(columns=['編號'])

# 顯示數據
print(df)

import folium

# 創建一個地圖對象，設置初始中心點為台灣（23.6978° N, 120.9605° E），初始縮放級別為7
m = folium.Map(location=[23.6978, 120.9605], zoom_start=7)

# 顯示地圖
m.save
