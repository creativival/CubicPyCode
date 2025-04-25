# 第8回：3Dアート：立体フラクタル図形の世界

![CubicPy Logo](https://creativival.github.io/CubicPyCode/assets/cubicpy_logo.png)

## 今日のミッション
**たった数行のコードから神秘的な立体フラクタルを作り出し、自分だけの3Dアート作品を創造しよう！**

## 前回のおさらい

前回は「3Dボーリングゲームを作ろう」と題して、APIモードを使った本格的なゲーム開発を学びました。ボーリングのピン配置、ボールの動き、そして得点計算など、ゲームの基本要素を実装しましたね。今回はAPIモードの知識をさらに発展させて、自然界にある美しいパターンを再現する「フラクタル図形」の世界に踏み込んでいきましょう！

## フラクタルとは？自然界に見られる不思議な形

### フラクタルの定義と特徴

フラクタルとは、部分が全体と同じような形を持つ「自己相似性」を特徴とする図形のことです。私たちの身の回りには、このフラクタルのパターンが多く存在しています。

- **木の枝分かれ**: 大きな枝から小さな枝が分かれ、さらに小さな枝が分かれるパターン
- **雪の結晶**: 六角形の中にさらに小さな六角形のパターンが現れる
- **シダの葉**: 葉全体の形と、その一部の形が似ている
- **山の稜線**: 大きなスケールでも小さなスケールでも似たようなデコボコが見られる

フラクタルの面白いところは、非常にシンプルなルールから複雑で美しい形が生まれる点です。今回はプログラミングでこのフラクタルを表現し、立体的な3Dアートを作成します。

> 💡 **先生からのヒント**: フラクタルは「自分自身を繰り返す」性質を持つパターンだよ。シンプルなルールから複雑な美しさが生まれるのが魅力なんだ！

## 再帰関数を使った立体フラクタルツリーの作り方

### 再帰関数とは？

再帰関数（さいきかんすう）とは、「関数の中で自分自身を呼び出す」という特殊な関数です。フラクタルのような「自己相似性」を持つパターンを表現するのに最適な方法なのです。

再帰関数は、以下の2つの重要な要素を持っています：

1. **基底条件（ベースケース）**: 再帰を終了させる条件
2. **再帰ステップ**: 自分自身を呼び出す部分（より小さな問題に分割）

例えば、フラクタルの木を描く場合：
- **基底条件**: 決められた回数、分岐したら終了
- **再帰ステップ**: より短い枝を異なる角度で描く

### 立体フラクタルツリーを描くコード

それでは、3D空間に立体的なフラクタルツリーを作成するコードを見てみましょう。以下のコードを `fractal_tree.py` という名前で保存してください。

```python
from cubicpy import CubicPyApp

app = CubicPyApp(gravity_factor=0.1, window_size=(1800, 1200))

# 座標系の変換を使って、簡単に複雑な構造を作る
def draw_branch(length, branch_count, branch_factor):
    if branch_count < 1:
        return

    # 木の幹を作成
    app.add_cylinder(
        position=(0, 0, 1),
        scale=(0.5, 0.5, length - 1),
        color=(0, 1, 0),
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
initial_length = 20      # 幹の長さ
max_branch_count = 6    # 枝分かれの最大回数
branch_factor = 0.6    # 枝の長さの縮小率

# 説明テキストを追加
app.set_top_left_text('フラクタルツリー')
app.set_bottom_left_text('代表的なフラクタル構造')

draw_branch(initial_length, max_branch_count, branch_factor)

app.run()
```

このコードを実行すると、3Dフラクタルツリーが表示されます。次のコマンドでプログラムを実行してみましょう。

```bash
python fractal_tree.py
```

![Fractal Tree](https://creativival.github.io/CubicPyCode/assets/fractal_tree_basic.png)

**▲図1▲ 基本的な3Dフラクタルツリー**

代表的なフラクタル構造である「フラクタルツリー」が作成されました（▲図1▲）。Zキーを押すと、デバッグ用の緑の線が非表示になり、オブジェクトの色がわかりやすくなります。

### コードの解説

このコードの中心となるのが、`draw_branch`という再帰関数です。詳しく見ていきましょう。

#### 1. 基底条件

```python
# 基底条件：再帰を終了する条件
if branch_count < 1:
    return
```

`branch_count`が1未満になると、関数は何もせずに終了します。これにより、無限に枝分かれし続けることを防ぎます。

#### 2. 枝（円柱）の作成

```python
    # 木の幹を作成
    app.add_cylinder(
        position=(0, 0, 1),
        scale=(0.5, 0.5, length - 1),
        color=(0, 1, 0),
        base_point=1  # 底面中心を基準に配置
    )
```

ここでは、円柱を使って木の幹や枝を表現しています。`scale` の長さを `length - 1` にすることで、次に配置するオブジェクトとの衝突を防止します。

#### 3. 座標変換と再帰呼び出し

```python
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
```

ここが再帰的なフラクタル生成の中心部分です：

1. `push_matrix()`で現在の座標系を保存
2. `translate()`で枝の先端まで移動
3. 次の枝の長さと分岐回数を計算
4. 3方向（120度ずつ）に回転させながら、より小さな枝を描画
5. 各枝を描画後、`pop_matrix()`で座標系を元に戻す

再帰的に関数が呼ばれることで、枝から枝が生え、さらにその枝から枝が生えるというフラクタルのパターンが形成されます。

> 🔍 **発見ポイント**: 再帰関数は自分自身を呼び出しますが、必ず「より小さな問題」に分解されていくことが重要です。このコードでは、`branch_count`を減らし、`length`を短くすることで、問題のサイズを小さくしています。

## 色のグラデーションとサイズ変化で美しさを演出

基本的なフラクタルツリーができたので、次は色とサイズのバリエーションを加えて、より美しいアート作品に仕上げましょう。以下のコードを `colorful_fractal_tree.py` という名前で保存してください。

```python
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
```

このコードを実行すると、色鮮やかな3Dフラクタルツリーが表示されます。

```bash
python colorful_fractal_tree.py
```

![Colorful Fractal Tree](https://creativival.github.io/CubicPyCode/assets/colorful_fractal_tree.png)

**▲図2▲ 色鮮やかな3Dフラクタルツリー**

### 改良点の解説

#### 1. 色のグラデーション

```python
# 分岐の深さに基づいて色を計算する関数
def calculate_branch_color(branch_count, max_count):
    # branch_countが大きいほど幹に近く、小さいほど先端に近い
    progress = 1.0 - (branch_count / max_count)  # 0.0(幹)から1.0(先端)の進行度
    
    # 赤から緑へのグラデーション
    red = 0.5 * (1.0 - progress)  # 0.5から0へ
    green = progress  # 0から1.0へ
    
    return (red, green, 0)
```

枝の深さ（`branch_count`）に応じて色相（hue）を変化させることで、根元から先端にかけてグラデーションを作り出しています。HSV色空間からRGB色空間への変換を行い、`progress`の値（0～1）に基づいて、茶色から緑に変化する色を計算しています。

> 💡 **先生からのヒント**: 自然界のフラクタルは完全に規則的ではなく、ランダム性やバリエーションがあります。少しの不規則性を加えることで、より自然で美しい形状になりますよ！

## フラクタルの他の形状：雪の結晶を作ってみよう

フラクタルは木だけでなく、様々な形状で表現できます。雪の結晶も美しいフラクタルパターンを持っています。以下のコードを `snowflake_fractal.py` という名前で保存してください。

```python
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
        position=(0, depth * 0.2, length * 0.1),
        scale=(0.2, 0.2,length * 0.8),
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
app.translate(0, 0, 20)  # 描き始めを高さ20に移動する
draw_snowflake(snowflake_size, snowflake_depth, snowflake_factor)
app.pop_matrix()
# シミュレーションを実行
app.run()
```

このコードを実行すると、フラクタルパターンを持つ雪の結晶が表示されます。

```bash
python snowflake_fractal.py
```

![Snowflake Fractal](https://creativival.github.io/CubicPyCode/assets/snowflake_fractal.png)

**▲図3▲ フラクタルパターンの雪の結晶**

```
# 6回対称の雪の結晶を描画する関数
def draw_snowflake(size, depth, factor):
    for i in range(6):
        app.push_matrix()
        app.rotate_hpr(0, 0, i * 60 + 30)  # Z軸周りに60度ずつ回転
        draw_snowflake_branch(size, depth, factor)
        app.pop_matrix()
```

雪の結晶のコードでは、6回対称性を表現するために、メインの関数（`draw_snowflake`）が6方向に分岐した枝（`draw_snowflake_branch`）を配置しています。`app.rotate_hpr(0, 0, i * 60 + 30)` により、Y軸中心で回転を行います。

各枝は再帰的にさらに小さな枝を生み出し、典型的な雪の結晶のパターンを形成します。

## チャレンジ：オリジナルの立体フラクタル作品を創ろう

今回学んだ再帰関数と座標変換の知識を使って、自分だけのオリジナルフラクタルアート作品を作りましょう！以下はいくつかのアイデアです：

1. **3Dシダの葉**: より複雑な枝分かれパターンを持つフラクタル
2. **立体的なコッホ曲線**: 直線が再帰的に折れ曲がるパターン
3. **ドラゴン曲線**: 折り紙を開いたような複雑なパターン
4. **シェルピンスキーの三角形**: 三角形の中に三角形が無限に現れるパターン

## デバッグのコツ

フラクタルプログラミングでよくあるデバッグの問題と解決策をいくつか紹介します：

1. **無限ループ**: 基底条件が正しく設定されていないと、プログラムが終わらなくなります。必ず終了条件を確認しましょう。
2. **メモリエラー**: 再帰が深すぎるとメモリ不足になることがあります。適切な深さ制限を設けましょう。
3. **座標変換のミスマッチ**: `push_matrix()`と`pop_matrix()`の数が一致していないと、オブジェクトが予期せぬ位置に配置されます。両方が対になっているか確認しましょう。
4. **パラメータの調整**: フラクタルは微妙なパラメータ調整で大きく形が変わります。少しずつ値を変えながら、望む形を探りましょう。

```python
# デバッグ用print文の例
def debug_recursive_function(depth):
    print(f"関数呼び出し：深さ = {depth}")
    
    if depth <= 0:
        print("基底条件に到達、終了します")
        return
    
    # 再帰呼び出し
    print(f"再帰呼び出し：深さ = {depth-1} を呼び出します")
    debug_recursive_function(depth - 1)
    print(f"深さ = {depth} の処理を完了しました")
```

## まとめ：今回学んだこと

1. **フラクタルの基本概念**: 自己相似性と自然界に見られるフラクタルパターン
2. **再帰関数のしくみ**: 基底条件と再帰ステップの重要性
3. **3Dフラクタルの作り方**: 立体的なフラクタルツリーや雪の結晶の作成方法
4. **色とバリエーション**: グラデーションや不規則性を加えて自然で美しい表現に
5. **座標変換の活用**: 複雑なフラクタルを表現するための座標系の操作

これらの技術を組み合わせることで、シンプルなコードから複雑で美しい3Dアート作品を生み出すことができます。

## 次回予告

次回は「Websocket通信でScratch3からCubicPyを操作する」をテーマに、プログラミング言語「Scratch」からCubicPyを操作する方法を学びます。Websocket通信の基本、Scratch3との連携方法、Scratch3を使った作品作りなど、新しい可能性を探っていきましょう！

> 🎨 **宿題（やってみよう）**: 今回学んだ再帰関数の知識を使って、自分だけのフラクタル作品を作ってみよう。色や形、分岐パターンを工夫して、友達に見せたくなるような美しい3Dアートを目指そう！

---

**キューパイでプログラミングを楽しもう！次回もお楽しみに！**