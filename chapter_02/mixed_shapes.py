# 物体データの配列を作成
body_data = []

# 床の箱を置く
body_data.append({
    'type': 'cube',
    'pos': (0, 0, 0),
    'scale': (5, 5, 0.5),  # 平たい箱
    'color': (0.5, 0.5, 0.5),  # グレー
    'mass': 0  # 質量0で動かないようにする
})

# 球を置く
body_data.append({
    'type': 'sphere',
    'pos': (0, 0, 3),
    'scale': (1, 1, 1),
    'color': (1, 0, 0)  # 赤
})

# 円柱を置く
body_data.append({
    'type': 'cylinder',
    'pos': (2, 0, 2),
    'scale': (0.5, 0.5, 2),  # 細長い円柱
    'color': (0, 1, 0)  # 緑
})