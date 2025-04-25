from math import cos, sin, radians
from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp()

# 壁を配置
for j in range(10):
    for i in range(-5, 5):
        app.add_cube(
            position=(i, 0, j),
            scale=(1, 1, 1),
            color=(1, 1, 1),  # 白
        )

# ボールを作成

ball_size = 1.8
ball_speed = 10
ball_angle = 15

app.add_sphere(
    position=(0, -30, 0),
    scale=(ball_size, ball_size, ball_size),
    color=(0.3, 0.3, 0.8),  # 青
    mass=10,
    velocity=(0, ball_speed * cos(radians(ball_angle)), ball_speed * sin(radians(ball_angle))),  # 前方向に発射
    base_point=1,  # 底面中心
)

# テキスト表示
app.set_top_left_text('壁破壊ゲーム')
app.set_bottom_left_text("操作方法: 矢印キーでカメラ移動、R でリセット")

# # アプリを実行
# app.run()

# ゲームロジックを追加して、移動したピンの数をスコア表示する
try:
    # ゲームロジックの初期化
    app.game_logic.target_type = 'cube'  # ターゲットをピンに設定
    app.game_logic.tolerance = 10  # 動いたとみなす閾値
    app.game_logic.motion_state = 'moved'  # 倒れた状態を監視

    # ゲームロジックの開始（サブスレッド）
    app.game_logic.start()

    # シミュレーションを実行（メインスレッド）
    app.run()
finally:
    # ゲームロジックの停止
    app.game_logic.stop()