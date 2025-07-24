from flask import Flask
"""
    It creates an instance of the Flask class,
    which will be your WSGI (Web Server Gateway Interface) apllication.
"""

##WSGI
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this flask code"

@app.route("/home")
def home():
    return "Welcome to this flask code !"


if __name__ == "__main__":
    app.run(debug=True)     #when debug is True simulatanious upedated the web server when we change the code
