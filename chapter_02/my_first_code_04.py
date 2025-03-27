# 物体データの配列を作成
body_data = []

# 10段の箱を積み上げる
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (0, 0, i),  # i の値が0から9まで変わる
        'scale': (1, 1, 1),
        'color': (1, 0, 0)  # すべて赤い箱
    })