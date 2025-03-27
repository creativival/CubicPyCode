# 物体データの配列を作成
body_data = []

# 左側のタワー（青から緑へ）
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (-3, 0, i),  # 左側の位置
        'scale': (1, 1, 1),
        'color': (0, i/10, 1-i/10),  # 青から緑へ
    })

# 右側のタワー（赤からオレンジへ）
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (3, 0, i),  # 右側の位置
        'scale': (1, 1, 1),
        'color': (1, i/10, 0),  # 赤からオレンジへ
    })