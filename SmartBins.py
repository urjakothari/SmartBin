import os,shutil,sys
from flask.json import dumps
from flask.json import JSONEncoder
from flask import Flask, request, redirect, url_for,render_template,jsonify,json
from werkzeug import secure_filename
from flask_jsglue import JSGlue
import csv
import psycopg2
import random

hostname = 'baasu.db.elephantsql.com'
username = 'pxzpxrfz'
password = 'mPamzjDlCoiNLEETVUVzGajAY5BSGf5q'
database = 'pxzpxrfz'
port='5432'

def databaseConnection():
	try:
		global myConnection
		myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database, port=port )
		global mark
		mark = myConnection.cursor() 
		#myConnection.close()
		print("Database Connection Sucessfully")
	except:
		print("Error")


app = Flask(__name__)
@app.route('/', methods=['GET','POST'])#this '/' will be the root ie it will display the home play of the website
def home():
	return render_template('SmartBins.html')

@app.route('/save')
def save():
	databaseConnection()
	print("abc1")
	Latitude = json.loads(request.args.get('latitude'))
	Longitude = json.loads(request.args.get('longitude'))
	n=len(Latitude)
	Filllevel=[]
	Gaslevel=[]
	for i in range(n):
		Filllevel.append(random.uniform(0.0, 1.0))
		Gaslevel.append(random.uniform(0.0,1.0))
	for i in range(n):
		statement='INSERT INTO public.dustbin (latitude,longitude,filllevel,gaslevel) VALUES ({},{},{},{})'.format(float(Latitude[i]),float(Longitude[i]),float(Filllevel[i]),float(Gaslevel[i]))
		mark.execute(statement)
		myConnection.commit()
	myConnection.close()	
	return jsonify(result=Latitude)


@app.route('/generateReport')
def generateReport():
	print("xyz")
	databaseConnection()
	threshold_filllevel=0.8
	threshold_gaslevel=0.6
	statement='SELECT binid,latitude,longitude FROM public.dustbin WHERE filllevel > 0.8  OR gaslevel > 0.6'#.format(threshold_filllevel,threshold_gaslevel)
	mark.execute(statement)
	result=mark.fetchall()
	print(result[0][0])
	json_array=[{"binid":r[0],"latitude":r[1],"longitude":r[2]} for r in result]
	print(json_array)
	#print(json.dumps(json_array))
	myConnection.commit()
	myConnection.close()
	print("ABC")	
	print(json.dumps(json_array))
	return jsonify(result=json_array)

@app.route('/markers')
def markers():	
	print("xyz123")
	databaseConnection()
	statement='SELECT latitude,longitude FROM public.dustbin'
	mark.execute(statement)
	result=mark.fetchall()
	#print(result[0][0])
	json_array=[{"latitude":r[0],"longitude":r[1]} for r in result]
	#print(json_array)
	#print(json.dumps(json_array))
	myConnection.commit()
	myConnection.close()
	print("ABC123")	
	#print(json.dumps(json_array))
	return jsonify(result=json_array)
