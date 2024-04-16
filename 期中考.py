import pandas as pd
import folium

# 讀取CSV文件，跳過第一行，並使用big5編碼
df = pd.read_csv('地震活動彙整_638488919649981406.csv', encoding='big5', skiprows=1)

# 創建一個地圖對象，設置初始中心點為台灣（23.6978° N, 120.9605° E），初始縮放級別為7
m = folium.Map(location=[23.6978, 120.9605], zoom_start=7)

# 遍歷數據框，為每個地點創建一個標記
for index, row in df.iterrows():
    # 獲取一個包含所有列名和值的字典
    info = row.to_dict()
    # 創建一個彈出視窗，內容為地點的所有信息，並使用HTML標籤來格式化文本
    popup_content = "<b>地點詳細信息:</b><br>" + "<br>".join([f"{key}: {value}" for key, value in info.items()])
    popup = folium.Popup(popup_content, max_width=300)
    # 創建一個標記，位置為地點的經緯度，並將彈出視窗添加到標記上
    marker = folium.Marker(location=[row['緯度'], row['經度']], popup=popup)
    # 將標記添加到地圖上
    marker.add_to(m)

# 保存地圖
m.save('地震活動地圖.html')