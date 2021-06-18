from flask_wtf import FlaskForm
# for string data field
from wtforms import StringField
# for validate the data :
from wtforms.validators import DataRequired,Length,Email,ValidationError # data required for not empty field and length for giving length cheks
# for email validation
import email_validator
# for password fields:
from wtforms import PasswordField
# for checking if password and confirm passwor are equal:
from wtforms.validators import EqualTo

# for submit field:
from wtforms import SubmitField
# boolean field 
from wtforms import BooleanField 
from flaskblog.models import User



# creating a registration form class for signup
#  flaskform is used for creating forms in flask:
class RegistrationForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired(),Length(min=2 , max= 20)])

	email =  StringField('Email',
		validators=[DataRequired(),Email()]) 

	password = PasswordField('Password',
		validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
		validators=[DataRequired(),EqualTo('password')])

	submit= SubmitField('Sign Up')

	def validate_username(self,username):
		user= User().query.filter_by(username= username.data).first()

		if user:
			raise ValidationError('That username already existed!')


	def validate_email(self,email):
		email= User().query.filter_by(email=email.data).first()

		if email:
			raise ValidationError('That Email already existed!')





# form for login :
class LoginForm(FlaskForm):

	email =  StringField('Email',
		validators=[DataRequired(),Email()]) 

	password = PasswordField('Password',
		validators=[DataRequired()])
	remember= BooleanField('Remember Me')
	submit= SubmitField('Login')

