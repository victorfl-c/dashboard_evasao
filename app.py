import streamlit as st
from modules.data_loader import load_data, load_original_data
from modules.filters import sidebar_filters, filter_dataframe
from modules.metrics import main_metrics
from modules.visuals import exploratory_tabs
from modules.risk_model import risk_tab
from modules.style import inject_custom_css
import pandas as pd

def main():
    
    inject_custom_css()
    df = load_data()
    filters = sidebar_filters(df)
    filtered_df = filter_dataframe(df, filters)
    st.title("📊 Dashboard de Análise de Evasão Estudantil")
    st.markdown("Análise explanatória dos fatores relacionados à evasão, conclusão e permanência de estudantes no ensino superior.")
    main_metrics(filtered_df)
    tab4 = exploratory_tabs(filtered_df)
    risk_tab(tab4, filters)
    st.markdown("---")
    st.markdown("**Dashboard desenvolvido por** Intellect.Ed | Dados atualizados em: {}".format(pd.to_datetime('today').strftime('%d/%m/%Y')))

if __name__ == "__main__":
    main()