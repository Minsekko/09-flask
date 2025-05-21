import pandas as pd
from sqlalchemy import create_engine
from prophet import Prophet
from sqlalchemy.testing import future
from flask import Flask,jsonify


def load_region_data(region) :
    engine = create_engine("mysql+pymysql://admin:1q2w3e4r@database.ch662qumapvg.ap-northeast-2.rds.amazonaws.com:3306/playground")

    sql = "select log_date as ds,"

    if region == "seoul" :
        sql += " seoul as y from dust_log order by log_date asc"
    else:
        sql += " gyeonggi as y from dust_log order by log_date asc"

    df = pd.read_sql(sql, engine)
    df["ds"] = pd.to_datetime(df["ds"])
    return df

def run_prophet(df, days=7) :
    model = Prophet(yearly_seasonality=True)
    model.fit(df)

    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    return forecast[["ds","yhat"]].tail(days)
