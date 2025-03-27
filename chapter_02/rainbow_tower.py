# 物体データの配列を作成
body_data = []

# 10段の箱を積み上げる（虹色）
for i in range(10):
    body_data.append({
        'type': 'cube',
        'pos': (0, 0, i),
        'scale': (1, 1, 1),
        'color': (i/10, 0, 1-i/10),  # 赤から紫へのグラデーション
    })