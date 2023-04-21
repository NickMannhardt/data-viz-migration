import os
import json
import numpy as np
import pandas as pd
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={r"*": {"origins": [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]}}
)

data_dir = './data/main_table.csv'

@app.route('/', methods=['GET'])
def index():
    return 'Server is active and running'

@app.route('/tipo_familia/<country>', methods=['GET'])
def get_tipo_familia(country):
    df = pd.read_csv(data_dir)
    columns = [
        'country',
        'tipo_familia'
    ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['tipo_familia'])\
        .count()\
        .rename({'country': 'count'}, axis=1)\
        .reset_index()
    print(df.to_json())
    return json.loads(df.to_json(orient='records', index=True))


@app.route('/avg_income_amount/<country>', methods=['GET'])
def get_avg_income_amount(country):
    df = pd.read_csv(data_dir)
    columns = [
        'country',
        'avg_income_amount'
    ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['avg_income_amount'])\
        .count()\
        .rename({'country': 'count'}, axis=1)\
        .reset_index()
    print(df.to_json())
    return json.loads(df.to_json(orient='records', index=True))

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080))
    )