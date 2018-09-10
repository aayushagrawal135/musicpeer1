from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm):
    email = StringField("Email ID", validators=[Email()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    re_password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign up")

    def match_passwords(self):
        return self.password.data == self.re_password.data
