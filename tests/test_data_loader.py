import pandas as pd
from modules.data_loader import load_data, load_original_data

def test_load_data_basic():
    df = load_data()
    assert isinstance(df, pd.DataFrame)
    assert "Matrícula" in df.columns
    assert "Status Acadêmico" in df.columns
    assert "Idade na Matrícula" in df.columns
    assert "Faixa Etária" in df.columns
    assert len(df) > 0
    # Test if mapping worked
    assert set(df["Status Acadêmico"].unique()).issubset({"Evadido", "Concluinte", "Matriculado"})

def test_load_original_data_basic():
    df = load_original_data()
    assert isinstance(df, pd.DataFrame)
    assert "Matrícula" in df.columns
    assert len(df) > 0