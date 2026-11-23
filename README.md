# Cat Panit Island（ホームページ素案）

ねこのかたちをした島のテーマパーク「Cat Panit Island」のホームページ素案です。料金・営業時間・アクセスなどはすべて仮の内容です。

## ファイル構成

- `index.html` — トップページ（CSS・JSを内包）
- `area-harbor.html` / `area-forest.html` / `area-hills.html` / `area-kotatsu.html` — 4つのエリアページ
- `assets/site.css`, `assets/area.js` — エリアページ共通のスタイルとスクリプト
- `assets/main-visual.svg` — メインビジュアル（`main-visual.png`, `main-visual@2x.png` はPNG版、`ogp.png` はSNSシェア用 1200×630）
- `tools/gen_areas.py` — エリアページの生成スクリプト

## エリアページの再生成

エリアページの内容は `tools/gen_areas.py` のデータから生成しています。変更するときはスクリプトを編集して、リポジトリのルートで実行してください。

```sh
python tools/gen_areas.py .
```

## 確認方法

ビルドは不要です。`index.html` をブラウザで直接開いて確認できます。
