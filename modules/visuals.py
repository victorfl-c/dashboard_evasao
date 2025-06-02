import streamlit as st
import plotly.express as px

def exploratory_tabs(filtered_df):
    st.header("📈 Distribuição Geral")
    tab1, tab2, tab3, tab4 = st.tabs(["Status Acadêmico", "Distribuição por Idade", "Gênero", "Risco"])
    with tab1:
        fig = px.pie(filtered_df, names='Status Acadêmico', title='Distribuição por Status Acadêmico',
                     color='Status Acadêmico', color_discrete_map={'Evadido': '#4fd0ca', 'Concluinte': '#267c79', 'Matriculado': '#38465c'})
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            fig = px.histogram(filtered_df, x="Idade na Matrícula", nbins=20, title="Distribuição por Idade", color_discrete_sequence=['#38465c'])
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.box(filtered_df, x="Status Acadêmico", y="Idade na Matrícula", title="Idade por Status Acadêmico",
                         color="Status Acadêmico", color_discrete_map={'Evadido': '#4fd0ca', 'Concluinte': '#267c79', 'Matriculado': '#38465c'})
            st.plotly_chart(fig, use_container_width=True)
    with tab3:
        fig = px.histogram(filtered_df, x="Status Acadêmico", color="Gênero_mapeado", barmode="group",
                           title="Distribuição por Gênero e Status", color_discrete_map={"Feminino": '#9599f5', "Masculino": '#267c79'})
        st.plotly_chart(fig, use_container_width=True)
    return tab4