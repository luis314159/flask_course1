from flask import Flask, request, redirect, make_response, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

bootstrap = Bootstrap(app)

#moment = Moment(app)

todo_list = ['Comprar cafe', 'Entrenar', 'Study']

app.config['SECRET_KEY'] = 'SUPER_SECRETEO'


class loginForm(FlaskForm):
    user_name= StringField('What is your user name?', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')

@app.route('/index', methods = ['GET', 'POST'])
def index():
    user_ip = session.get('user_ip')
    login_form = loginForm()
    user_name = session.get('user_name')

    context = {
       'user_ip': user_ip,
       'todo_list': todo_list,
       'login_form': login_form,
       'user_name': user_name
    }
    if login_form.validate_on_submit():
       user_name = login_form.user_name.data
       session['user_name'] = user_name

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
    app.run(debug=True)