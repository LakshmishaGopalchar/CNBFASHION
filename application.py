import pyodbc
import pandas as pd
import pyodbc
from flask import Flask
from flask import Flask, jsonify
#import spacy
from flask import request

server = 'MAFVDCBISQL03'
database = 'MAFVCUSTDW'
#username = 'aateam'
#password = 'uKPdyRRNEK7qQ9xS'
#driver= '{ODBC Driver 17 for SQL Server}'
drivers = [item for item in pyodbc.drivers()]
driver = drivers[-1]
#sql_conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=MAFVDCBISQL03;DATABASE=MAFVCUSTDW;Trusted_Connection=yes') 

cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()


cursor.execute("Select * from DimDate")
row = cursor.fetchone()

#while row:
#    print (str(row[0]) + " " + str(row[1]))
#    row = cursor.fetchone()

app = Flask(__name__)

app.debug = True

#app.run(debug=False)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/jsonResrNew")
def helloNew():
    
    return (str(row[0])) 
