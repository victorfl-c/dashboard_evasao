import streamlit as st

def sidebar_filters(df):
    with st.sidebar:
        st.title("Filtros")
        age_range = st.slider("Faixa Etária", int(df["Idade na Matrícula"].min()), int(df["Idade na Matrícula"].max()), (18, 30))
        academic_status = st.multiselect("Status Acadêmico", options=df["Status Acadêmico"].unique(), default=df["Status Acadêmico"].unique())
        scholarship_filter = st.multiselect("Bolsa de Estudos", options=df["Bolsista_mapeado"].unique(), default=df["Bolsista_mapeado"].unique())
        gender_filter = st.multiselect("Gênero", options=df["Gênero_mapeado"].unique(), default=df["Gênero_mapeado"].unique())
        risco_evasao_range = st.slider(
            "Risco de Evasão (%)", 
            min_value=0, 
            max_value=100, 
            value=(0, 100)
        )
    filters = {
        "age_range": age_range,
        "academic_status": academic_status,
        "scholarship_filter": scholarship_filter,
        "gender_filter": gender_filter,
        "risco_evasao_range": risco_evasao_range
    }
    return filters

def filter_dataframe(df, filters):
    return df[
        (df["Idade na Matrícula"] >= filters["age_range"][0]) &
        (df["Idade na Matrícula"] <= filters["age_range"][1]) &
        (df["Status Acadêmico"].isin(filters["academic_status"])) &
        (df["Bolsista_mapeado"].isin(filters["scholarship_filter"])) &
        (df["Gênero_mapeado"].isin(filters["gender_filter"]))
    ]