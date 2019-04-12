from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/validate", methods=['POST'])                                    
    
def validate():

    password_error = ''
    password = request.form['password']
    if (' ' in password) == True:
        password_error = "Your password cannot contain spaces or be left blank."     
    if len(password) < 3 or len(password) > 20:
        password_error = "Your password must be between 3 and 20 characters."

    password_same_error = ''
    password_user_verified = request.form['password_user_verified']
    password = request.form['password']
    if password != password_user_verified:
        password_same_error = "Passwords do not match."

    username_error = ''
    username = request.form['username']
    if (' ' in username) == True:                                             
        username_error = "Your username cannot contain spaces or be left blank."    
    if len(username) < 3 or len(username) > 20:
        username_error = "Your username must be between 3 and 20 characters."   

    email_error = ''
    email = request.form['email']
    num_ats = email.count('@')
    num_periods = sum([char == '.' for char in email])   
    if num_ats != 1 or num_periods != 1:
        email_error = "Please enter a valid email address."
    if (' ' in email) == True:
        email_error = "Please enter a valid email address."
    if len(email) < 3 or len(email) > 20:
        email_error = "Please enter a valid email address."
    if len(email) == 0:
        email_error = ''
    
    if email_error == '' and username_error == '' and password_error == '' and password_same_error == '':
        return render_template("welcome.html", username = username)               
    
    else:
        return render_template("index.html", email = email, username = username,
        password_same_error = password_same_error, password_error = password_error,  
        email_error = email_error, username_error = username_error)
       

@app.route("/")
def index():
    return render_template("index.html")

app.run()