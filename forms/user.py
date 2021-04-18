from flask_wtf import FlaskForm
import wtforms
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    """Форма регистрации"""
    email = EmailField('Введите почту', validators=[DataRequired()])
    password = PasswordField('Введите пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Введите имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Расскажите немного о себе")
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    """Форма авторизации"""
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class EditForm(FlaskForm):
    """Форма редактирования"""
    name = StringField('Имя', validators=[DataRequired()])
    about = TextAreaField('Описание', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
