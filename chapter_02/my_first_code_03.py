# 物体データの配列を作成
body_data = []

# 赤い箱
body_data.append({
    'type': 'cube',
    'pos': (-2, 0, 0),  # 左側
    'scale': (1, 1, 1),
    'color': (1, 0, 0)  # 赤
})

# 緑の箱
body_data.append({
    'type': 'cube',
    'pos': (0, 0, 0),  # 中央
    'scale': (1, 1, 1),
    'color': (0, 1, 0)  # 緑
})

# 青い箱
body_data.append({
    'type': 'cube',
    'pos': (2, 0, 0),  # 右側
    'scale': (1, 1, 1),
    'color': (0, 0, 1)  # 青
})