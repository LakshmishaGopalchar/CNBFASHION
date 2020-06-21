import pyodbc
import pandas as pd
import pyodbc
from flask import Flask
from flask import Flask, jsonify
#import spacy
from flask import request
import turicreate as tc

server = 'MAFVAZEBISQL01'
database = 'TX_MAFFashionDW'
#username = 'aateam'
#password = 'uKPdyRRNEK7qQ9xS'
#driver= '{ODBC Driver 17 for SQL Server}'
drivers = [item for item in pyodbc.drivers()]
driver = drivers[-1]
print(driver)

app = Flask(__name__)

app.debug = True

#app.run(debug=False)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/jsonResrNew")
def helloNew():
    
    return (("succesfully inserted")) 
