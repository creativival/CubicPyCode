from math import sqrt

body_data = []
step_num = 20  # 段数

# ピラミッドの各辺を作成
for i in range(step_num):
  # 数学的に正確なピラミッドの形を計算
  x = (step_num - (i + 1)) / sqrt(3)
  y = x
  z = i

  # 4つの辺を作成
  pos = (x, y, z)
  body_data.append({
    'type': 'box',
    'pos': pos,
    'scale': (1, 1, 1),
    'color': (1, 0, 0),
    'mass': 1
  })

  # 頂点以外の場所では、残りの3辺も作成
  if i != step_num - 1:
    pos = (-x, y, z)
    body_data.append({
      'type': 'box',
      'pos': pos,
      'scale': (1, 1, 1),
      'color': (1, 0, 0),
      'mass': 1
    })

    pos = (x, -y, z)
    body_data.append({
      'type': 'box',
      'pos': pos,
      'scale': (1, 1, 1),
      'color': (1, 0, 0),
      'mass': 1
    })

    pos = (-x, -y, z)
    body_data.append({
      'type': 'box',
      'pos': pos,
      'scale': (1, 1, 1),
      'color': (1, 0, 0),
      'mass': 1
    })