import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    df = pd.read_csv('data/dataset_risco_matriculados.csv')
    df["Matrícula"] = ["MAT%05d" % i for i in range(1, len(df) + 1)]
    df.rename(columns={
        'Target': 'Status Acadêmico',
        'Age at enrollment': 'Idade na Matrícula',
        'Scholarship holder': 'Bolsista',
        'Gender': 'Gênero'
    }, inplace=True)
    df['Status Acadêmico'] = df['Status Acadêmico'].map({
        'Dropout': 'Evadido',
        'Graduate': 'Concluinte',
        'Enrolled': 'Matriculado'
    })
    encoder = LabelEncoder()
    df['Status Acadêmico_encoded'] = encoder.fit_transform(df['Status Acadêmico'])
    bins = [15, 20, 25, 30, 35, 40, 50, 70]
    labels = ["15-19", "20-24", "25-29", "30-34", "35-39", "40-49", "50+"]
    df["Faixa Etária"] = pd.cut(df["Idade na Matrícula"], bins=bins, labels=labels, right=False)
    df['Gênero_mapeado'] = df['Gênero'].map({0: "Feminino", 1: "Masculino"})
    df['Bolsista_mapeado'] = df['Bolsista'].map({0: "Não", 1: "Sim"})
    return df

def load_original_data():
    df = pd.read_csv('data/dataset_risco_matriculados.csv')
    df["Matrícula"] = ["MAT%05d" % i for i in range(1, len(df) + 1)]
    return df