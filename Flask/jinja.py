## Building URL dynamically
## Variable rule
## Jinja 2 Tempalate Engine

### Jinja 2 Template Engine
'''
    {{  }} expressions to print output in html
    {{%...%}} conditions , for loops
    {#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect, url_for
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

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


# ========================================= VARIABLE RULE ===========================================
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is " + str(score)

@app.route('/test/<int:score>')
def test(score):
    res=""
    if score >= 50:
        res="Pass"
    else:
        res="Fail"
    return render_template('result.html',results=res)



@app.route('/loop/<int:score>')
def loop(score):
    res=""
    if score >= 50:
        res="Pass"
    else:
        res="Fail"
    
    exp={'score':score,"res":res}
    return render_template('result1.html',results=exp)


@app.route('/if/<int:score>')
def if_test(score):
    res=""
    
    return render_template('result2.html',results=score)

@app.route('/getresult',methods=['POST','GET'])
def getresult():
    total_score = 0
    if request.method=="POST":
        science = float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('test',score=total_score))

    

if __name__ == "__main__":
    app.run(debug=True)     #when debug is True simulatanious upedated the web server when we change the code