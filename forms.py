from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    subtitle = StringField("Подзаголовок", validators=[DataRequired()])
    img_url = StringField("Картинка фона", validators=[DataRequired(), URL()])
    body = CKEditorField("Информация в посте", validators=[DataRequired()])
    submit = SubmitField("Обубликовать")

class User(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField("Адрес эл. почты", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")


class CommentForm(FlaskForm):
    body = CKEditorField("Комментарий", validators=[DataRequired()])
    submit = SubmitField("Опубликовать")

