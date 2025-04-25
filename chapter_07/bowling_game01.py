from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 簡単なボウリングゲームのセットアップ
# ピンを配置
pin_positions = [
    (0, 0, 0),  # 1番ピン（先頭）
    (-1, 1, 0), (1, 1, 0),  # 2-3番ピン
    (-2, 2, 0), (0, 2, 0), (2, 2, 0),  # 4-6番ピン
    (-3, 3, 0), (-1, 3, 0), (1, 3, 0), (3, 3, 0),  # 7-10番ピン
]

for pos in pin_positions:
    app.add_cylinder(
        position=(pos[0], pos[1], 0),
        scale=(0.8, 0.8, 3.2),
        color=(1, 1, 1),  # 白
        base_point=1,  # 底面中心
    )

# ボールを作成
ball_size = 1.8
ball_speed = 10

app.add_sphere(
    position=(0, -20, 0),
    scale=(ball_size, ball_size, ball_size),
    color=(0.3, 0.3, 0.8),  # 青
    mass=10,
    velocity=(0, ball_speed, 0),  # 前方向に発射
    base_point=1,  # 底面中心
)

# テキスト表示
app.set_top_left_text('ボウリングゲーム')
app.set_bottom_left_text("操作方法: 矢印キーでカメラ移動、R でリセット")

# アプリを実行
app.run()