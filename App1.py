from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome"

@app.route('/member')
def welcome1():
    return "Aao sa"





if __name__ == '__main__':
    app.run(debug=True)