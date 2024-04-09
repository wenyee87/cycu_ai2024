import pandas as pd

# 檔案路徑
file_path = '/workspaces/cycu_ai2024/20240409/地震活動彙整_638482866006340637.csv'

try:
    # 讀取 CSV 檔案，使用 'big5' 編碼，跳過第一行
    data = pd.read_csv(file_path, encoding='big5', skiprows=1)

    # 移除 "編號" 和 "深度" 這兩列
    data = data.drop(['編號', '深度'], axis=1)

    # 輸出資料
    print(data)
except FileNotFoundError as e:
    print("File not found:", str(e))


import folium

# 創建一個地圖物件
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 為資料中的每一行添加一個標記
for index, row in data.iterrows():
    # 創建一個彈出窗口，顯示該位置的所有資料
    popup = folium.Popup(str(row), parse_html=True)
    
    folium.Marker(
        location=[row['緯度'], row['經度']],
        popup=popup,  # 將彈出窗口添加到標記中
    ).add_to(m)

# 顯示地圖
m.save('/workspaces/cycu_ai2024/20240409/地震活動彙整_638482866006340637.html')