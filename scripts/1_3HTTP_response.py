from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/')
def index():
 return '<h1>Bad Request</h1>', 400

if __name__ =='__main__':
    app.run(debug=True)
