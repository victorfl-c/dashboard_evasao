import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import joblib
import os
from modules.data_loader import load_original_data

def risk_tab(tab, filters):
    with tab:
        st.subheader("⚠️ Probabilidade de Evasão dos Alunos Matriculados")
        df_model_orig = load_original_data()
        df_train_model = df_model_orig[df_model_orig['Target'] != "Enrolled"].copy()
        df_train_model['Target_bin'] = df_train_model['Target'].map({'Dropout': 1, 'Graduate': 0})
        X_train = df_train_model.drop(columns=['Target', 'Target_bin', 'Matrícula'])
        y_train = df_train_model['Target_bin']
        # Teste
        df_test_model = df_model_orig[df_model_orig['Target'] == "Enrolled"].copy()
        gender_map_reverse = {"Feminino": 0, "Masculino": 1}
        scholarship_map_reverse = {"Não": 0, "Sim": 1}
        df_test_model = df_test_model[
            (df_test_model["Age at enrollment"] >= filters["age_range"][0]) &
            (df_test_model["Age at enrollment"] <= filters["age_range"][1]) &
            (df_test_model["Gender"].isin([gender_map_reverse[g] for g in filters["gender_filter"]])) &
            (df_test_model["Scholarship holder"].isin([scholarship_map_reverse[s] for s in filters["scholarship_filter"]]))
        ]
        X_test = df_test_model.drop(columns=["Target", "Matrícula"], errors="ignore")

        model_option = st.selectbox("Modelo:", ["Regressão Logística", "Random Forest", "SVM"])
        model_map = {
            "Regressão Logística": LogisticRegression(max_iter=1000),
            "Random Forest": RandomForestClassifier(n_estimators=100),
            "SVM": SVC(probability=True)
        }
        model_name = model_option.replace(" ", "_").lower()
        model_filename = f"modelo_{model_name}.pkl"
        if os.path.exists(model_filename):
            pipeline = joblib.load(model_filename)
        else:
            pipeline = make_pipeline(StandardScaler(), model_map[model_option])
            pipeline.fit(X_train, y_train)
            joblib.dump(pipeline, model_filename)

        if X_test.shape[0] == 0:
            st.warning("⚠️ Nenhum estudante 'Matriculado' encontrado com os filtros de idade, gênero e bolsa. Ajuste os filtros na sidebar.")
        else:
            probas = pipeline.predict_proba(X_test)[:, 1]
            df_test_model["Risco de Evasão (%)"] = (probas * 100).round(1)
            df_test_model = df_test_model[
                (df_test_model["Risco de Evasão (%)"] >= filters["risco_evasao_range"][0]) &
                (df_test_model["Risco de Evasão (%)"] <= filters["risco_evasao_range"][1])
            ]
            if df_test_model.shape[0] == 0:
                st.warning("⚠️ Nenhum estudante 'Matriculado' encontrado com os filtros de risco de evasão selecionados. Ajuste o slider.")
            else:
                st.markdown("### 📊 Distribuição do Risco de Evasão")
                fig = px.histogram(df_test_model, x="Risco de Evasão (%)", nbins=20, color_discrete_sequence=["#0084a5"])
                fig.update_layout(title="Distribuição do Risco de Evasão (%)")
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("### 📈 Risco Médio por Faixa Etária")
                bins = [15, 20, 25, 30, 35, 40, 50, 70]
                labels = ["15-19", "20-24", "25-29", "30-34", "35-39", "40-49", "50+"]
                df_test_model["Faixa Etária"] = pd.cut(df_test_model["Age at enrollment"], bins=bins, labels=labels, right=False).astype(str)
                risco_medio = df_test_model.groupby("Faixa Etária")["Risco de Evasão (%)"].mean().reset_index()
                fig = px.bar(risco_medio, x="Faixa Etária", y="Risco de Evasão (%)", color="Risco de Evasão (%)", color_continuous_scale="teal")
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("### 🧾 Estudantes com Maior Risco")
                df_export = df_test_model.copy()
                df_export['Gênero'] = df_export['Gender'].map({0: "Feminino", 1: "Masculino"})
                df_export['Bolsista'] = df_export['Scholarship holder'].map({0: "Não", 1: "Sim"})
                df_export.rename(columns={'Age at enrollment': 'Idade na Matrícula'}, inplace=True)
                st.dataframe(df_export[["Matrícula", "Idade na Matrícula", "Gênero", "Bolsista", "Risco de Evasão (%)"]]
                            .sort_values("Risco de Evasão (%)", ascending=False).reset_index(drop=True))
                csv_export = df_export[["Matrícula", "Idade na Matrícula", "Gênero", "Bolsista", "Risco de Evasão (%)"]].to_csv(index=False).encode('utf-8')
                st.download_button("📥 Baixar CSV de Estudantes em Risco", data=csv_export, file_name="estudantes_em_risco.csv", mime="text/csv")
