# 物体データの配列を作成
body_data = []

# 箱を1つ追加
body_data.append({
    'type': 'cube',  # 形は立方体（箱）
    'pos': (0, 0, 0),  # 位置: x, y, z
    'scale': (1, 1, 1),  # サイズ: 幅, 奥行き, 高さ
    'color': (1, 0, 0)  # 色: 赤, 緑, 青 (0〜1)
})