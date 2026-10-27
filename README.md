# 福井県 自転車盗難マップ

## 起動（Windows PowerShell）

```powershell
cd bicycle_theft_map
py -m pip install -r requirements.txt
py app.py
```

ブラウザで http://127.0.0.1:5000 を開いてください。

CSVは `data/thefts.csv` に配置済みです。インターネット接続が必要です（地図タイル・Leafletの読み込み）。

※データの座標は実際の事件発生地点ではなく代表地点の可能性があります。公開する場合は出典、利用条件、プライバシーへの配慮を確認してください。Flaskのdebugモードを有効にしたまま公開しないでください。
