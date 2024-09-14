from flask import Flask, request, redirect, make_response, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

todo_list = ['Comprar cafe', 'Entrenar', 'Study']

app.config['SECRET_KEY'] = 'SUPER_SECRETEO'

@app.route('/')
def index():
    user_ip = session.get('user_ip')
    context = {
       'user_ip': user_ip,
       'todo_list' : todo_list 
    }
    return render_template('index.html', **context)

@app.route('/bad_request')
def bad_request():
 return '<h1>Bad Request</h1>', 400


@app.route("/ip_request")
def ip_request():
    user_ip = request.remote_addr
    response = make_response(redirect('/'))
    #response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/ip_print')
def print_ip():
    user_ip = request.cookies.get('user_ip')

    return '<p>Your IP is: %s</p>' % user_ip

@app.errorhandler(404)
def not_found(error):
   return render_template('404.html', error = error)

@app.errorhandler(500)
def internal_error(error):
 return render_template('500.html', error = error)

if __name__ =='__main__':
    app.run(debug=True )
