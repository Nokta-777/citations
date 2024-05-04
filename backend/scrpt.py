from flask import Flask, request

app = Flask(__name__)

@app.route('/',method=["POST","GET"])
def index():
    return "hello world"

@app.route('/hello/<name>')
def hey(name):
    return f"hello {name}"

@app.route('/add/<int:para1>/<int:para2>')
def add(para1, para2):
    return f"{para1+para2}"

@app.route('/help')
def help():
    return request.args()
    

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)