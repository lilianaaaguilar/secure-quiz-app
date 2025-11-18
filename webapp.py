import os
import time
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
	session["startTime"] = time.time()
	return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
	if "firstResponse" not in session:
		session["firstResponse"]=request.form['firstResponse']
	return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
	if "secondResponse" not in session:
		session["secondResponse"]=request.form['secondResponse']
	return render_template('page3.html')

@app.route('/page4',methods=['GET','POST'])
def renderPage4():
	if "thirdResponse" not in session:
		session["thirdResponse"]=request.form['thirdResponse']
	return render_template('page4.html')
    
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
	if "fourthResponse" not in session:
		session["fourthResponse"]=request.form['fourthResponse']
	return render_template('page5.html')
    
@app.route('/page6',methods=['GET','POST'])
def renderPage6():
    if "fifthResponse" not in session:
        session["fifthResponse"]=request.form['fifthResponse']
    session["endTime"] = time.time()
    score = 0
    if session["firstResponse"].lower() == "egg":
	    answer1="Correct"
	    score=score+1
    else:
	    answer1="Incorrect"
        
    if session["secondResponse"] == "12" or session["secondResponse"].lower() == "twelve":
        answer2="Correct"
        score=score+1
    else:
    	answer2="Incorrect"
    
    if session["thirdResponse"].lower() == "age":
        answer3="Correct"
        score=score+1
    else:
        answer3="Incorrect"
        
    if session["fourthResponse"].lower() == "darkness":
        answer4="Correct"
        score=score+1
    else:
        answer4="Incorrect"
        
    if session["fifthResponse"].lower() == "cold":
        answer5="Correct"
        score=score+1
    else:
       answer5="Incorrect"
         
    timeTaken = session["endTime"] - session["startTime"]
    return render_template('page6.html', answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5, score=score, timeTaken=timeTaken)
    
if __name__=="__main__":
    app.run(debug=False)
