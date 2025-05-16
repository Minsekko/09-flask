import pandas as pd

def load_data() :
    return pd.read_csv("data/hospitals-2025.csv")

def count_hospital_type() :
    df = load_data()
    tp = df.groupby("종별코드명").size()
    result = []
    for i in tp.index:
        result.append({"label": i, "value": int(tp[i])})

    return result