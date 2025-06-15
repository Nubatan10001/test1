import pandas as pd

df = pd.read_csv("2025-06-13.csv")

translated_columns = {}

# AチームとBチームのプレイヤーデータ
for team in ['A', 'B']:
    for i in range(1, 5):
        prefix = f'{team}{i}'
        translated_columns[f'{prefix}-weapon'] = f'{prefix}のブキ'
        translated_columns[f'{prefix}-kill-assist'] = f'{prefix}のキル＋アシスト'
        translated_columns[f'{prefix}-kill'] = f'{prefix}のキル数'
        translated_columns[f'{prefix}-assist'] = f'{prefix}のアシスト数'
        translated_columns[f'{prefix}-death'] = f'{prefix}のデス数'
        translated_columns[f'{prefix}-special'] = f'{prefix}のスペシャル発動数'
        translated_columns[f'{prefix}-inked'] = f'{prefix}の塗りポイント'
        translated_columns[f'{prefix}-abilities'] = f'{prefix}のギアパワー'

# メダル情報
for i in range(1, 4):
    translated_columns[f'medal{i}-grade'] = f'メダル{i}のグレード'
    translated_columns[f'medal{i}-name'] = f'メダル{i}の名称'

# 基本情報
translated_columns.update({
    '# season': 'シーズン',
    'period': '試合期間',
    'game-ver': 'ゲームバージョン',
    'lobby': 'ロビー種類',
    'mode': 'ルール',
    'stage': 'ステージ名',
    'time': '試合時間',
    'win': '勝敗',
    'knockout': 'ノックアウト勝ち',
    'rank': 'ランク',
    'power': 'パワー',
    'alpha-inked': 'Aチームの塗りポイント',
    'alpha-ink-percent': 'Aチームの塗り割合（%）',
    'alpha-count': 'Aチームの人数',
    'alpha-color': 'Aチームのインク色',
    'alpha-theme': 'Aチームのテーマ',
    'bravo-inked': 'Bチームの塗りポイント',
    'bravo-ink-percent': 'Bチームの塗り割合（%）',
    'bravo-count': 'Bチームの人数',
    'bravo-color': 'Bチームのインク色',
    'bravo-theme': 'Bチームのテーマ',
    'event': 'イベント情報'
})

# 列名を日本語に変換
df_renamed = df.rename(columns=translated_columns)


df_renamed.to_csv("2025-06-13_prep.csv", index=False)