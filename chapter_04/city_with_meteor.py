# create_city_100x100.pyのコードをここにコピー

# 隕石を生成
body_data.append({
    'type': 'sphere',
    'pos': (CITY_WIDTH / 2, CITY_LENGTH / 2, 200),  # 都市の中心上空に配置
    'scale': (50, 50, 50),  # 直径100のかなり大きな球体
    'color': (1, 1, 1),  # 白色
    'mass': 100,  # 重い質量を設定
    'base_point': 2,  # 重心を基準に配置
    'velocity': (0, 0, -100),  # 下向きに高速で移動（スペースキーで発射）
})