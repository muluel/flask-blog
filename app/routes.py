from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# Url setting
@app.route('/')
@app.route('/index')

# index view
def index():
    
    user = {'username' : 'Muhammed'}
    posts=[
        {
            'author':{'username':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author':{'username':'Susan'},
            'body': 'The Avangers movie was so cool!'
        }
    ]
    # view leri render ederek son hallerinin ne olmasini soyler
    return render_template('index.html', title='Home', user=user, posts=posts)

#login sayfasi icin url
@app.route('/login', methods=['GET','POST'])
# login formunun view yapisi
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)