import pandas as pd
from modules.risk_model import risk_tab

def test_risk_tab_runs(monkeypatch):
    # Patch everything from Streamlit and joblib to avoid side effects
    monkeypatch.setattr("streamlit.subheader", lambda *a, **k: None)
    monkeypatch.setattr("streamlit.selectbox", lambda *a, **k: "Regressão Logística")
    monkeypatch.setattr("streamlit.warning", lambda *a, **k: None)
    monkeypatch.setattr("streamlit.markdown", lambda *a, **k: None)
    monkeypatch.setattr("streamlit.plotly_chart", lambda *a, **k: None)
    monkeypatch.setattr("streamlit.dataframe", lambda *a, **k: None)
    monkeypatch.setattr("streamlit.download_button", lambda *a, **k: None)

    class DummyTab:
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_val, exc_tb): pass

    # Dummy filters (should match keys used in risk_tab)
    filters = {
        "age_range": (18, 30),
        "academic_status": ["Matriculado"],
        "scholarship_filter": ["Sim"],
        "gender_filter": ["Feminino"],
        "risco_evasao_range": (0, 100)
    }
    # Just check if the function runs (does not raise)
    risk_tab(DummyTab(), filters)