# importing models :
# it will be import here bcos db is used in user,post which is created after db : so when db is created then we user
# post models:
from flask import render_template,url_for,flash,redirect
from flaskblog import app,db,bcrypt
from flaskblog. models import User,Post
from flaskblog.form import RegistrationForm,LoginForm
from flask_login import login_user,current_user,logout_user,login_required
from flask import request


posts=[
{ "author": "Anuj Yadav",
   "title": "Blog post 1",
   "content": "Blog content 1",
   "date_posted": "25/05/2021"   
},	
{ "author": "kittu",
   "title": "Blog post 2",
   "content": "Blog content 2",
   "date_posted": "26/05/2021"   
}	
]


@app.route('/')
@app.route('/home')
def home():
	return render_template('homeroute.html',posts=posts,title="Blog Page")


@app.route('/about')
def about():
	return render_template('Aboutroute.html',title="About Page")


# route for a Registration:
@app.route('/register',methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form= RegistrationForm()
	if form.validate_on_submit():
		hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user= User(username=form.username.data,email= form.email.data, password= hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Your Account has been created!','success')
		return redirect(url_for('login'))

	return	render_template('register.html',title='Register',form=form)

# route for  login form:

@app.route('/login',methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form= LoginForm()

	if form.validate_on_submit():
		user= User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember= form.remember.data)
			next_page= request.args.get('next')
			if next_page:
				return redirect(next_page)
			return redirect(url_for('home'))
		else:
			flash(f'Wrong Email or  password','danger')

    		
	return render_template('login.html',title='Login',form=form)

#logout route if user is logged in
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))	

# account route:
@app.route('/account')
@login_required
def account():
	return render_template('account.html',title='Accounts')
	
