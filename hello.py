from flask import Flask, request, json
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html');



@app.route('/signIn', methods=['POST'])
def userSignIn():
    username = request.form['username'];
    password = request.form['password'];
    if username == 'admin@admin.com' and password == 'admin':
	return json.dumps({'html':'<span id="res">User found :)</span>'});
    else:
	return json.dumps({'html':'<span id="res">User not found</span>'});


    

@app.route('/signUp',methods=['POST'])
def SignUp():
    username = request.form['username'];
    password = request.form['password'];
    return json.dumps({'html':'User registration successful'});

if __name__ == "__main__":
    app.debug = True
    app.run()
