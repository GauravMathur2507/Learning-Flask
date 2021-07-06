from flask import Flask, redirect, url_for,request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('mainn.html')



@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('result.html', result= res)


@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        datascience = float(request.form['datascience'])
        c = float(request.form['C'])
        maths = float(request.form['maths'])
        total_score = (science+datascience+c+maths)/4
    
    return redirect(url_for('success', score = total_score))

    


if __name__ == '__main__':
    app.run(debug = True)