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
        "http://nickmannhardt.github.io",
        "https://nickmannhardt.github.io"
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
    print(df)
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

@app.route('/saving_months/<country>', methods=['GET'])
def get_saving_months(country):
    df = pd.read_csv(main_data_dir)
    columns = [
        'country',
        'saving_months'
    ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['saving_months'])\
        .count()\
        .rename({'country': 'count'}, axis=1)\
        .reset_index()
    df2 = df['saving_months'].mean()
    return jsonify({'result':int(df2)})

@app.route('/debt_months/<country>', methods=['GET'])
def get_debt_months(country):
    df = pd.read_csv(main_data_dir)
    columns = [
        'country',
        'debt_months'
    ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['debt_months'])\
        .count()\
        .rename({'country': 'count'}, axis=1)\
        .reset_index()
    df2 = df['debt_months'].mean()
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

@app.route('/econ_condition/<country>/<rsp_sex>', methods=['GET'])
def get_econ_condition(country,rsp_sex):
    df = pd.read_csv(main_data_dir)
    print(f"rsp_sex:{rsp_sex}")
    # apply the age and gender filter to calculate the highest preocupaciones_first
    df = df[ (df['rsp_sex'] == int(rsp_sex))] #(df['rsp_age'] == 10) this is too narrow

    columns = [
            'country',
            'econ_condition'
        ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['econ_condition'])\
            .count()\
            .rename({'country': 'count'}, axis=1)\
            .reset_index()

    index = df['count'].idxmax()
    econ_condition= df['econ_condition'][index ]
    return jsonify({'result':int(econ_condition)})

@app.route('/remesa_parentesco/<country>/<rsp_sex>', methods=['GET'])
def get_remesa_parentesco(country,rsp_sex):
    df = pd.read_csv(main_data_dir)
    print(f"rsp_sex:{rsp_sex}")
    # apply the age and gender filter to calculate the highest preocupaciones_first
    df = df[ (df['rsp_sex'] == int(rsp_sex))] #(df['rsp_age'] == 10) this is too narrow

    columns = [
            'country',
            'remesa_parentesco'
        ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['remesa_parentesco'])\
            .count()\
            .rename({'country': 'count'}, axis=1)\
            .reset_index()

    index = df['count'].idxmax()
    remesa_parentesco= df['remesa_parentesco'][index ]
    return jsonify({'result':int(remesa_parentesco)})

@app.route('/remesa_remit_ocupacion/<country>/<rsp_sex>', methods=['GET'])
def get_remesa_remit_ocupacion(country,rsp_sex):
    df = pd.read_csv(main_data_dir)
    print(f"rsp_sex:{rsp_sex}")
    # apply the age and gender filter to calculate the highest preocupaciones_first
    df = df[ (df['rsp_sex'] == int(rsp_sex))] #(df['rsp_age'] == 10) this is too narrow

    columns = [
            'country',
            'remesa_remit_ocupacion'
        ]
    df = df[columns]
    df = df[df['country'] == country]
    df = df.groupby(['remesa_remit_ocupacion'])\
            .count()\
            .rename({'country': 'count'}, axis=1)\
            .reset_index()

    index = df['count'].idxmax()
    remesa_remit_ocupacion= df['remesa_remit_ocupacion'][index ]
    return jsonify({'result':int(remesa_remit_ocupacion)})

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

@app.route('/final_remesa_amount/<country>/<rsp_age>/<rsp_sex>', methods=['GET'])
def get_final_remesa_amount(country, rsp_age,rsp_sex):
    df = pd.read_csv(main_data_dir)

    rsp_age = int(rsp_age)

    # Create a new column that groups ages into 10-year intervals
    df['age_bracket'] = pd.cut(df['rsp_age'], bins=range(0, 121, 10))

    # Define the desired age bracket based on a numeric age value
    age_bracket = pd.Interval((rsp_age//10)*10, ((rsp_age//10)*10)+10)

    columns = [
            'country',
            'remesa_amount',
            'age_bracket',
            'rsp_sex']

    df = df[ (df['country'] == country) & (df['rsp_sex'] == int(rsp_sex))& (df['age_bracket'] == age_bracket )]

    df = df[columns]
    df = df.dropna()

    df = df.groupby(['remesa_amount'])\
            .count()\
            .rename({'country': 'count'}, axis=1)\
            .reset_index()
    df['remesa_bracket'] = pd.cut(df['remesa_amount'], bins=range(0, int(df['remesa_amount'].max()) + 51, 50), right=False)

    df = df.groupby(['remesa_bracket'])\
        .count()\
        .rename({'count': 'count'}, axis=1)\
        .reset_index()

    total_remesas = df['count'].sum()
    df['remesa_pct'] = (df['count'] / total_remesas * 100).astype(int)

    df = df[['remesa_bracket','remesa_pct']]
    df['remesa_bracket'] = df['remesa_bracket'].apply(lambda x:  int(x.right))
    print(df)
    return json.loads(df.to_json(orient='records', index=True))




#External Migration Dataset
@app.route('/mig_ext_violence_who/<rsp_sex>', methods=['GET'])
def get_mig_ext_violence(rsp_sex):
    df = pd.read_csv(ext_data_dir)
    # df = df.where(df['country'] == country)
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
    df['count'] = df['count'] / df['count'].sum() * 100
    
    df = df.sort_values('count', ascending=False)

    return json.loads(df.to_json(orient='records', index=True))

@app.route('/mig_ext_violence/<country>/<rsp_sex>', methods=['GET'])
def get_mig_ext_violence_country(country, rsp_sex):
    df = pd.read_csv('data/mig_ext_roster.csv')
    df = df.where(df['country'] == country)

    columns = [
        'mig_ext_sex',
        *[x for x in df.columns if x.startswith('mig_ext_violence/')]
    ]

    df = df[columns]

    df['count'] = 1

    df = df.dropna()
    df = df.groupby('mig_ext_sex').sum()
    df = (df / sum(df['count']) * 100)
    # .astype({col: 'int' for col in columns[1:]})
    a = json.loads(df.to_json(index=True))
    return [{
        'label': key.split('/')[-1],
        'value': sum([v for v in a[key].values()]),
        'highlight': a[key][f'{int(rsp_sex)}.0']
    } for key, value in a.items()]


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

@app.route('/mig_ext_attempts_counts/<country>/<rsp_age>/<rsp_sex>', methods=['GET'])
def get_mig_ext_attempts_counts(country, rsp_age, rsp_sex):
    df = pd.read_csv(ext_data_dir)
    df = df.where(df['country'] == country)
    rsp_age = int(rsp_age)
    df['age_bracket'] = pd.cut(df['mig_ext_age'], bins=range(0, 121, 10))
    age_bracket = pd.Interval((rsp_age//10)*10, ((rsp_age//10)*10)+10)
    filtered = df[(df['mig_ext_sex'] == int(rsp_sex)) & (df['age_bracket'] == age_bracket)]

    columns = ['mig_ext_attempts', 'age_bracket']
    df = df[columns]
    filtered = filtered[columns]

    total = list(df.groupby(['mig_ext_attempts']).count()['age_bracket'])
    f = list(filtered.groupby(['mig_ext_attempts']).count()['age_bracket'])

    out = []

    for i in range(len(total)):
        out.append({
            'label': i+1,
            'value': (total[i] / sum(total) * 100),
            'highlight': (f[i] / sum(total) * 100) if i < len(f) else 0
        })
    return out


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080))
    )