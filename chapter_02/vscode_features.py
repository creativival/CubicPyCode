body_data = []

# エラーの例と修正
# エラー: カンマが抜けている
body_data.append({
    'type': 'cube'  # ここにカンマが必要
    'pos': (0, 0, 0)
})

# 修正版
body_data.append({
    'type': 'cube',  # カンマを追加
    'pos': (0, 0, 0)
})