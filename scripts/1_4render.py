from flask import Flask, request, redirect, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.cookies.get('user_ip')

    return render_template('index.html', user_ip = user_ip)

@app.route('/bad_request')
def bad_request():
 return '<h1>Bad Request</h1>', 400


@app.route("/ip_request")
def ip_request():
    user_ip = request.remote_addr
    response = make_response(redirect('/ip_print'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/ip_print')
def print_ip():
    user_ip = request.cookies.get('user_ip')
    return '<p>Your IP is: %s</p>' % user_ip

if __name__ =='__main__':
    app.run(debug=True)
