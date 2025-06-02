import streamlit as st

def main_metrics(filtered_df):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Estudantes", len(filtered_df))
    with col2:
        st.metric("Taxa de Evasão", f"{len(filtered_df[filtered_df['Status Acadêmico'] == 'Evadido'])/len(filtered_df)*100:.1f}%" if len(filtered_df) else "0%")
    with col3:
        st.metric("Taxa de Conclusão", f"{len(filtered_df[filtered_df['Status Acadêmico'] == 'Concluinte'])/len(filtered_df)*100:.1f}%" if len(filtered_df) else "0%")
    with col4:
        st.metric("Bolsistas", f"{len(filtered_df[filtered_df['Bolsista'] == 1])/len(filtered_df)*100:.1f}%" if len(filtered_df) else "0%")