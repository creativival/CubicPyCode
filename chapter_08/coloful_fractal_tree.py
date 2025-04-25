from cubicpy import CubicPyApp

app = CubicPyApp(gravity_factor=0.1, window_size=(1800, 1200))

# 最大繰り返し回数をグローバル変数として定義
max_branch_count = 6

# 分岐の深さに基づいて色を計算する関数
def calculate_branch_color(branch_count, max_count):
    # branch_countが大きいほど幹に近く、小さいほど先端に近い
    progress = 1.0 - (branch_count / max_count)  # 0.0(幹)から1.0(先端)の進行度
    
    # 赤から緑へのグラデーション
    red = 0.5 * (1.0 - progress)  # 0.5から0へ
    green = progress  # 0から1.0へ
    
    return (red, green, 0)

# 座標系の変換を使って、簡単に複雑な構造を作る
def draw_branch(length, branch_count, branch_factor):
    if branch_count < 1:
        return

    # 色と太さを計算
    color = calculate_branch_color(branch_count, max_branch_count)
    
    # 木の幹を作成
    app.add_cylinder(
        position=(0, 0, 1),
        scale=(0.5, 0.5, length - 1),
        color=color,
        base_point=1  # 底面中心を基準に配置
    )

    # 次の枝の分岐点まで移動
    app.push_matrix()
    app.translate(0, 0, length)

    # 複数の枝を作成
    branch_length = length * branch_factor
    branch_count -= 1

    # 3方向に枝を伸ばす
    for angle in [0, 120, 240]:
        app.push_matrix()
        app.rotate_hpr(angle, 30, 0)  # Y軸周りに角度を変え、X軸周りに30度傾ける
        draw_branch(branch_length, branch_count, branch_factor)
        app.pop_matrix()

    app.pop_matrix()


# 木を描画
initial_length = 20     # 幹の長さ
branch_factor = 0.6     # 枝の長さの縮小率

# 説明テキストを追加
app.set_top_left_text('グラデーションフラクタルツリー')
app.set_bottom_left_text('赤から緑へ色が変化するフラクタル構造')

draw_branch(initial_length, max_branch_count, branch_factor)

app.run()