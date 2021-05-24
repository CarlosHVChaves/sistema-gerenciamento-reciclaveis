from flask_wtf import FlaskForm
from email_validator import validate_email
from flask_wtf.recaptcha import validators
from wtforms.fields import (
    BooleanField, 
    PasswordField, 
    StringField,
    SubmitField, 
    SelectField
)
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import (
    DataRequired, 
    Email,
    Length
)
from app.models import Book


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email(validate_email)
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters.")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        DataRequired("O campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email(validate_email)
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters.")
    ])
    submit = SubmitField("Cadastrar")


class BookForm(FlaskForm):
    name = StringField("Nome do livro", validators=[
        DataRequired("O campo é obrigatório")
    ])
    submit = SubmitField("Salvar")

class MaterialForm(FlaskForm):
    name = StringField(u"Nome do Material", validators=[
        DataRequired("O campo é obrigatório")
    ])
    sector = SelectField(u"Setores", choices=[
        ("Papel"), ("Plástico"), ("Metal"), ("Vidro")
    ], validators=[
        DataRequired("É obrigatório escolher uma das opções")
    ])
    quantidade = IntegerField(u"Quantidade", validators=[
        DataRequired("O campo é obrigatório")
    ])
    submit = SubmitField("Salvar")


class UserBookForm(FlaskForm):
    book = SelectField("Livro", coerce=int)
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book.choices = [ 
            (book.id, book.name) for book in Book.query.all()
        ]