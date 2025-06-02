import pandas as pd
from modules.filters import filter_dataframe

def test_filter_dataframe_basic():
    # Dummy DataFrame for testing
    df = pd.DataFrame({
        "Idade na Matrícula": [18, 22, 29, 35],
        "Status Acadêmico": ["Evadido", "Concluinte", "Matriculado", "Evadido"],
        "Bolsista_mapeado": ["Sim", "Não", "Sim", "Não"],
        "Gênero_mapeado": ["Feminino", "Masculino", "Feminino", "Masculino"]
    })
    filters = {
        "age_range": (20, 30),
        "academic_status": ["Evadido", "Matriculado"],
        "scholarship_filter": ["Sim"],
        "gender_filter": ["Feminino"],
        "risco_evasao_range": (0, 100)
    }
    filtered = filter_dataframe(df, filters)
    assert isinstance(filtered, pd.DataFrame)
    # Should return only row index 2
    assert len(filtered) == 1
    assert filtered.iloc[0]["Status Acadêmico"] == "Matriculado"