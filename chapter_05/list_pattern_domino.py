body_data = []

# 迷路のサイズとパターン
list_pattern = [
    "000000000011111111111",
    "000000000100000000000",
    "000000001000000000000",
    "000000010000000000000",
    "000000101000000000000",
    "000001000100000000000",
    "000010000011111111111",
    "000100000000000000000",
    "001000000000000000000",
    "010000000000000000000",
    "100000000000000000000",
    "010000000000000000000",
    "001000000000000000000",
    "000100000000000000000",
    "000010000011111111111",
    "000001000100000000000",
    "000000101000000000000",
    "000000010000000000000",
    "000000001000000000000",
    "000000000100000000000",
    "000000000011111111111",
]

# ドミノの設定
spacing = 1.0  # ドミノ間の距離
domino_width = 1.0
domino_height = 2.0
domino_thickness = 0.2

# リストからドミノの配置を生成
num_list = len(list_pattern)
for i, row in enumerate(list_pattern):
    y = (num_list - i - 1) * domino_width / 2   # 上から下に向かうため、y座標を反転

    for j, dot in enumerate(list(row)):
        if dot == '1':
            body_data.append({
                'type': 'cube',
                'pos': (j * spacing, y, 0),
                'scale': (domino_thickness, domino_width, domino_height),
                'color': (1, 0, 0),
                'mass': 10 if j == 0 else 1,  # 最初のドミノは重めにして倒しやすくする
                'velocity': (2, 0, 0) if j == 0 else (0, 0, 0),
            })
            