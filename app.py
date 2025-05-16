#pip install flask
#pip install numpy
#pip install pandas
#pip install flask-cors
from datetime import datetime
from flask import Flask, request
import numpy as np
import pandas as pd
from flask import Flask,request
from flask_cors import CORS
from flask_cors import cross_origin
import util

import util

in_memory_db =[]

app = Flask(__name__)
CORS(app,origins="*")

@app.get("/api/hospital/groups")
def hospital_groups_handel() :
    response = util.count_hospital_type()
    return response, 200

@app.post("/api/numpy")
def numpy_handle() :
    a = np.array(request.json["data"])
    #return {"mean" : np.mean(a), "max" : np.max(a), "min" : np.min(a)}
    return {"mean": float(np.mean(a)), "max": float(np.max(a)), "min": float(np.min(a)) }

@app.get("/api/health")
def health_handle() :
    return {"status" : True}

@app.post("/api/report")
def report_handle() :
    print(request.json)

@app.post("/api/fruit")
def fruit_post_handle() :
    one = { "name" : request.json["name"], "create_at" : datetime.now()}
    print(request.json, type(request.json))
    in_memory_db.append(one)
    return one, 201

@app.get("/api/fruit")
def fruit_get_handle() :
    return in_memory_db