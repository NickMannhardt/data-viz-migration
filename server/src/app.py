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

main_data_dir = './data/main_table.csv'
ext_data_dir = './data/mig_ext_roster.csv'


@app.route('/', methods=['GET'])
def index():
    return 'Server is active and running'

#Main Table Migration Dataset
@app.route('/tipo_familia/<country>', methods=['GET'])
def get_tipo_familia(country):
    df = pd.read_csv(main_data_dir)
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
    return json.loads(df.to_json(orient='records', index=True))


@app.route('/avg_income_amount/<country>', methods=['GET'])
def get_avg_income_amount(country):
    df = pd.read_csv(main_data_dir)
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
    return json.loads(df.to_json(orient='records', index=True))

@app.route('/mean_income_amount/<country>', methods=['GET'])
def get_mean_income_amount(country):
    df = pd.read_csv(main_data_dir)
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
    df = pd.read_csv(main_data_dir)
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


@app.route('/preocupaciones_first/<country>/<rsp_sex>', methods=['GET'])
def get_preocupaciones_first(country,rsp_sex):
    df = pd.read_csv(main_data_dir)
    print(f"rsp_sex:{rsp_sex}")
    # apply the age and gender filter to calculate the highest preocupaciones_first
    df = df[ (df['rsp_sex'] == int(rsp_sex))] #(df['rsp_age'] == 10) this is too narrow

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

@app.route('/remesa_amount/<country>/<rsp_age>/<rsp_sex>', methods=['GET'])
def get_remesa_amount(country, rsp_age,rsp_sex):
    # apply the age and gender filter to calculate the mean remesa for that demographic
    df = pd.read_csv(main_data_dir)
    df = df[(df['rsp_age'] >= int(rsp_age) - 10) & (df['rsp_age'] <= int(rsp_age) + 10) & (df['rsp_sex'] == int(rsp_sex))]

    columns = [
            'country',
            'remesa_amount'
        ]
    df = df[columns]
    df = df[df['country'] == country]

    remesa = df['remesa_amount'].mean()

    r = df['remesa_amount'].mean()
    remesa = (str(r))

    if remesa== "nan":
            remesa = "0"
    else :
            r = int(r)
            remesa = (str(r))

    print(f"remesa amount, slide 2:{remesa}")

    return jsonify({'result':str(remesa)})

#External Migration Dataset
@app.route('/mig_ext_violence/<rsp_sex>', methods=['GET'])
def get_mig_ext_violence(rsp_sex):
    df = pd.read_csv(ext_data_dir)
    df = df[ (df['mig_ext_sex'] == int(rsp_sex))] #(df['rsp_age'] == 10) this is too narrow
    columns = [
                'mig_ext_sex',
                'mig_ext_violence_who'
            ]
    df = df[columns]

    #percentage of people who suffered from violence
    num_nan = df['mig_ext_violence_who'].isna().sum()
    num_rows = df.shape[0]
    perc_nan = num_nan/num_rows
    perc_violence = round(((1-perc_nan)*100),1)

    df = df.groupby(['mig_ext_violence_who'])\
                .count()\
                .rename({'mig_ext_sex': 'count'}, axis=1)\
                .reset_index()
    
    index = df['count'].idxmax()
    highest_violence = df['mig_ext_violence_who'][index ]
    print(perc_violence)
    print(highest_violence)

    return jsonify({'highest_violence_group':str(highest_violence),'perc_violence': float(perc_violence) })


@app.route('/mig_ext_attempts/<rsp_age>/<rsp_sex>', methods=['GET'])
def get_mig_ext_attempts(rsp_age,rsp_sex,):
     # Read the data into a dataframe
    df = pd.read_csv(ext_data_dir)

    rsp_age = int(rsp_age)

    # Create a new column that groups ages into 10-year intervals
    df['age_bracket'] = pd.cut(df['mig_ext_age'], bins=range(0, 121, 10))

    # Define the desired age bracket based on a numeric age value
    age_bracket = pd.Interval((rsp_age//10)*10, ((rsp_age//10)*10)+10)

    # Apply the age and gender filter
    df = df[(df['mig_ext_sex'] == int(rsp_sex)) & (df['age_bracket'] == age_bracket)]

    # Select the desired columns
    columns = [ 'mig_ext_attempts', 'age_bracket']
    df = df[columns]


    # Group the data by attempts and age bracket, and count the number of occurrences
    df = df.groupby(['mig_ext_attempts'])\
                .count()\
                .rename({'age_bracket': 'count'}, axis=1)\
                .reset_index()

    # Calculate total count
    total_count = df['count'].sum()

    # Calculate the percentage of each count value over the total number of counts
    perc = []
    attempt_counts = [1, 2, 3,4,5]
    for attempt in attempt_counts:
        if attempt not in df['mig_ext_attempts'].values:
            df = df.append({'mig_ext_attempts': attempt, 'count': 0}, ignore_index=True)
        count = df[df['mig_ext_attempts'] == attempt]['count'].iloc[0]
        percentage = (count / total_count) * 100
        perc.append(percentage)
    return jsonify({'perc1':round(perc[0],1),'perc2':round(perc[1],1),'perc3':round(perc[2],1),'perc4plus':round((perc[3]+perc[4]),1)})




if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080))
    )