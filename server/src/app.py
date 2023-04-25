import os
import json
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
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

@app.route('/mean_income_amount/<country>', methods=['GET'])
def get_mean_income_amount(country):
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
    df2 = df['avg_income_amount'].mean()
    return jsonify({'result':int(df2)})

@app.route('/debt_amount/<country>', methods=['GET'])
def get_debt_amount(country):
    df = pd.read_csv(data_dir)
    columns = [
        'country',
        'debt_amount'
    ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['debt_amount'])\
        .count()\
        .rename({'country': 'count'}, axis=1)\
        .reset_index()
    df2 = df['debt_amount'].mean()
    return jsonify({'result':int(df2)})


@app.route('/preocupaciones_first/<country><rsp_age><rsp_sex>', methods=['GET'])
def get_preocupaciones_first(country, rsp_age,rsp_sex):
    df = pd.read_csv(data_dir)

    # apply the age and gender filter to calculate the highest preocupaciones_first
    df = df[(df['rsp_age'] == rsp_age) & (df['rsp_sex'] == rsp_sex)]

    columns = [
            'country',
            'preocupaciones_first'
        ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['preocupaciones_first'])\
            .count()\
            .rename({'country': 'count'}, axis=1)\
            .reset_index()

    index = df['count'].idxmax()
    highest_preocc = df['preocupaciones_first'][index ]
    return jsonify({'result':str(highest_preocc)})



if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080))
    )