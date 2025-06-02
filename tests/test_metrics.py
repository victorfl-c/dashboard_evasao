import pandas as pd
from modules.metrics import main_metrics

def test_main_metrics_runs(monkeypatch):
    # Creates a dummy DataFrame
    df = pd.DataFrame({
        "Status Acadêmico": ["Evadido", "Concluinte", "Matriculado", "Evadido"],
        "Bolsista": [1, 0, 1, 0]
    })
    # Patch streamlit columns and metric to not actually display
    monkeypatch.setattr("streamlit.columns", lambda n: [DummyCol() for _ in range(n)])
    monkeypatch.setattr("streamlit.metric", lambda *a, **k: None)
    main_metrics(df)

class DummyCol:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass
    def metric(self, *a, **k): pass