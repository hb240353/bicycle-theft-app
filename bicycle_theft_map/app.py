from flask import Flask, render_template, jsonify, request
import csv
from pathlib import Path

app = Flask(__name__)
DATA = Path(__file__).parent / 'data' / 'thefts.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/incidents')
def incidents():
    city = request.args.get('city', '')
    lock = request.args.get('lock', '')
    records = []
    with DATA.open(encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f):
            if city and row['市区町村（発生地）'] != city: continue
            if lock and row['施錠関係'] != lock: continue
            try:
                lat, lng = float(row['緯度']), float(row['経度'])
            except (ValueError, TypeError): continue
            if not (35.0 <= lat <= 37.0 and 135.0 <= lng <= 138.0): continue
            records.append({'lat':lat,'lng':lng,'city':row['市区町村（発生地）'], 'address':row['フル住所'], 'date':row['発生年月日（始期）'], 'time':row['発生時（始期）'], 'place':row['発生場所'], 'detail':row['発生場所の詳細'], 'lock':row['施錠関係']})
    return jsonify(records)

if __name__ == '__main__':
    app.run(debug=True)
