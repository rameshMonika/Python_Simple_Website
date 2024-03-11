from flask import Flask, render_template, request


app = Flask(__name__)
name="Ramesh Monika"
age=12
qualification="software engineer"
list=['usa','ue','pak','ind','uae']

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/about')
def about():
    return render_template("/about.html",name=name,age=age,qualification=qualification,li=list)


@app.route('/',methods=['POST'])
def getdata():
   name=request.form['name']
   age=request.form['age']
   db=request.form['dateofbirth']
   return render_template('pass.html',n=name,a=age,d=db)


if __name__=="__main__":
    app.debug = True
    app.run()