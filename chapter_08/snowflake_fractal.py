from cubicpy import CubicPyApp

# アプリケーションのインスタンスを作成
app = CubicPyApp(gravity_factor=0, window_size=(1200, 900))

# 雪の結晶の枝を描画する再帰関数
def draw_snowflake_branch(length, depth, factor):
    # 基底条件：再帰を終了する条件
    if depth <= 0:
        return
    
    # メインの枝を作成
    app.add_cube(
        position=(0, depth * 0.2, length  * 0.1),
        scale=(0.2, 0.2,length  * 0.8),
        color=(0.9, 0.9, 1.0),  # 白色（青みがかった）
        base_point=1  # 底面中心を基準に配置
    )
    
    # 次の枝の分岐点まで移動
    app.push_matrix()
    app.translate(0, 0, length)
    
    # 6方向に小さな枝を伸ばす（雪の結晶の特徴）
    side_length = length * factor
    app.push_matrix()
    draw_snowflake(side_length, depth - 1, factor)
    app.pop_matrix()
    
    app.pop_matrix()

# 6回対称の雪の結晶を描画する関数
def draw_snowflake(size, depth, factor):
    for i in range(6):
        app.push_matrix()
        app.rotate_hpr(0, 0, i * 60 + 30)  # Z軸周りに60度ずつ回転
        draw_snowflake_branch(size, depth, factor)
        app.pop_matrix()

# テキスト表示
app.set_top_left_text('フラクタル雪の結晶')
app.set_bottom_left_text('矢印キーでカメラ移動、SHIFT+WASDQE でカメラ位置移動')

# 雪の結晶のパラメータ
snowflake_size = 10    # 枝の長さ
snowflake_depth = 3   # 再帰の深さ
snowflake_factor = 0.4

# 雪の結晶を描画
app.push_matrix()
app.translate(0, 0, 20)
draw_snowflake(snowflake_size, snowflake_depth, snowflake_factor)
app.pop_matrix()
# シミュレーションを実行
app.run()