#Vamos a crear las funciones de nuestro proyecto

import pandas as pd

def limpieza_dataset(df):
    df.columns = df.columns.str.replace("_", " ")

    if "Salary USD" in df.columns:
        df["Salary USD"] = df["Salary USD"].round(2)

    if "Job Title" in df.columns:
        df["Job Title"] = df["Job Title"].str.title()

    if 'AI Workload Ratio' in df.columns:
        df['AI Workload Ratio'] = pd.to_numeric(df['AI Workload Ratio'], errors='coerce')

    if "AI Impact" in df.columns:
        df["AI Impact"] = df["AI Impact"].str.replace("%", "", regex=False)
        df['AI Impact'] = df['AI Impact'].astype(str).astype(float)

