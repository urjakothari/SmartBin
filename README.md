# SmartBin
Two modules 
1. Flask App :

   -> This app is on Server side .
   -> ProcFile and Requirements.txt is created for deploying flask app on heroku
   -> For run this app :
 	local host :
		Enter these commands in terminal(Tested in Ubuntu)
		export FLASK_APP=SmartBins.py
		export FLASK_DEBUG=1
		python -m flask run

       Global Server Url:
		https://bin-flaskapp.herokuapp.com/

2. Android App :

    -> Install apk and run.

We have generated real time dustbin data in DustbinData.csv. We used this data randomly in our project.

There are two columns in DustbinData.csv

1. Gas level(in ppm)
2. Height (in cm) :
	By using sensor we get Height of remaining part
	requiredHeight = DustbinHeight - value
	

We have hosted our database in elephantsql cloud

To view Database type this command in terminal :

 psql postgres://pxzpxrfz:mPamzjDlCoiNLEETVUVzGajAY5BSGf5q@baasu.db.elephantsql.com:5432/pxzpxrfz

(postgres installation required)


	
