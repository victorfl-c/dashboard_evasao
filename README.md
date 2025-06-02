# 📊 Dashboard de Análise de Evasão Estudantil

Este projeto é um dashboard interativo desenvolvido em [Streamlit](https://streamlit.io/) para análise de evasão estudantil, permitindo explorar dados, visualizar métricas e avaliar o risco de evasão dos alunos a partir de diferentes modelos preditivos.

---

## 🗂️ Estrutura do Projeto

```
dashboard/
│
├── app.py                       # Arquivo principal Streamlit (entrypoint)
├── style.css                    # Estilos customizados (CSS)
├── requirements.txt             # Dependências do projeto
├── data/
│   └── dataset_risco_matriculados.csv
├── modules/
│   ├── __init__.py
│   ├── data_loader.py           # Funções de carregamento e preparação dos dados
│   ├── filters.py               # Funções dos filtros da sidebar
│   ├── metrics.py               # Funções das métricas principais
│   ├── visuals.py               # Funções dos gráficos exploratórios
│   ├── risk_model.py            # Funções do modelo preditivo de risco
│   └── style.py                 # Função para injeção do CSS customizado
└── tests/
    ├── __init__.py
    ├── test_data_loader.py
    ├── test_filters.py
    ├── test_metrics.py
    ├── test_visuals.py
    └── test_risk_model.py
```

---

## 🚀 Como Executar

1. **Clone o repositório e acesse a pasta:**
   ```bash
   git clone https://github.com/victorfl-c/dashboard_evasao.git
   cd dashboard_evasao
   ```

2. **Crie um ambiente virtual e instale as dependências:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows

   pip install -r requirements.txt
   ```

3. **Execute o aplicativo Streamlit:**
   ```bash
   streamlit run app.py
   ```

4. **Acesse o dashboard:**  
   Abra no navegador o endereço exibido pelo Streamlit (por padrão http://localhost:8501).

---

## 📂 Organização dos Módulos

- **app.py**  
  Ponto de entrada do dashboard. Orquestra o carregamento de dados, aplicação dos filtros, visualização das métricas, gráficos e análise de risco.

- **modules/data_loader.py**  
  Funções para carregar, preparar e transformar os dados.

- **modules/filters.py**  
  Funções que implementam a sidebar e a filtragem do DataFrame conforme os parâmetros escolhidos.

- **modules/metrics.py**  
  Funções para calcular e exibir as principais métricas do painel.

- **modules/visuals.py**  
  Funções para os gráficos exploratórios (distribuição, idade, gênero, etc).

- **modules/risk_model.py**  
  Funções para treinar e aplicar modelos preditivos de risco de evasão, exibir gráficos e permitir download de resultados.

- **modules/style.py**  
  Função para injeção do CSS customizado (presente em `styles.css`).

- **styles.css**  
  Arquivo com as regras de CSS customizadas para visual do dashboard.

- **tests/**  
  Pasta com testes automatizados para cada módulo do projeto, utilizando `pytest`.

---

## 🧪 Testes

Os testes estão localizados na pasta `tests/`, com um arquivo para cada módulo.  
Para rodar todos os testes, execute:

```bash
pytest
```

Os testes verificam:
- Se os dados são carregados corretamente,
- Se os filtros estão funcionando,
- Se as funções de métrica e visualização executam sem erros,
- Se a lógica de risco/modelo está operacional.

---

## 🏷️ Requisitos

- Python 3.8+
- Streamlit
- Pandas
- Plotly
- scikit-learn
- joblib
- (ver demais em `requirements.txt`)

---

## 🎨 Personalização Visual (CSS)

O dashboard utiliza um arquivo `styles.css` para customizar as cores, bordas, sliders, abas e outros elementos do Streamlit, garantindo identidade visual própria e experiência aprimorada.

---

## 🏗️ Boas Práticas

- **Modularização:** O código está organizado em módulos separados por responsabilidade, facilitando manutenção e escalabilidade.
- **Testes:** Cada módulo possui testes automatizados, seguindo a prática de TDD.
- **Reutilização:** Funções autônomas possibilitam reaproveitamento em outros projetos ou notebooks.
- **Separação de estilo:** O CSS está centralizado, desacoplado da lógica da aplicação.

---

## 🤝 Contribuição

Pull requests são bem-vindos!  
Sugira melhorias, reporte bugs ou contribua com novas funcionalidades.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 📬 Contato

Dúvidas, sugestões ou consultoria:  
**Intellect.Ed** – [victorcosta.contact@gmail.com]

---
