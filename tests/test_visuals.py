import pandas as pd
from modules.visuals import exploratory_tabs

def test_exploratory_tabs_runs(monkeypatch):
    # Minimal DataFrame to avoid plotly errors
    df = pd.DataFrame({
        "Status Acadêmico": ["Evadido", "Concluinte"],
        "Idade na Matrícula": [18, 22],
        "Gênero_mapeado": ["Feminino", "Masculino"]
    })
    # Patch streamlit plotting/charting functions
    monkeypatch.setattr("streamlit.header", lambda *a, **k: None)
    monkeypatch.setattr("streamlit.tabs", lambda labels: [DummyTab() for _ in labels])
    monkeypatch.setattr("streamlit.plotly_chart", lambda *a, **k: None)
    exploratory_tabs(df)

class DummyTab:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass