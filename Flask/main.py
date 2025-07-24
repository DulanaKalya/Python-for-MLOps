from flask import Flask,render_template
"""
    It creates an instance of the Flask class,
    which will be your WSGI (Web Server Gateway Interface) apllication.
"""

##WSGI
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course.</H1></html"

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return "<h2 style='font-family: Calibri, sans-serif;'>This is the About page.</h2>ß"


if __name__ == "__main__":
    app.run(debug=True)     #when debug is True simulatanious upedated the web server when we change the code
