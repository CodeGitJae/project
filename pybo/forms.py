from flask_wtf  import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class QuestionForm(FlaskForm):
    subject = StringField("제목", validators=[DataRequired("제목은 필수 입력 항목입니다.")])
    content = TextAreaField("내용", validators=[DataRequired("내용은 필수 입력 항목입니다.")])
    user_id = StringField("작성자",  validators=[DataRequired("로그인 후 사용하세요.")]) # 추가
    file_path = StringField("첨부파일")

class AnswerForm(FlaskForm):
    content = TextAreaField("내용", validators=[DataRequired("내용은 필수 입력 항목입니다.")])
    user_id = StringField("작성자", validators=[DataRequired("로그인 후 사용하세요.")]) # 추가


class UserCreateForm(FlaskForm):
    username = StringField("사용자이름", validators=[DataRequired("아이디 입력은 필수 항목입니다."), Length(min=3, max=20)])
    password1 = PasswordField("비밀번호", validators=[DataRequired("비밀번호 입력은 필수 항목 입니다."), EqualTo("password2","비밀번호가 일치하지 않습니다.")])
    password2 = PasswordField("비밀번호(확인)", validators=[DataRequired("비밀번호를 검증하세요.")])
    email = EmailField("이메일", validators=[DataRequired("이메일을 입력하세요."), Email()])

class UserLoginForm(FlaskForm):
    username = StringField("사용자이름", validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField("비밀번호", validators=[DataRequired()])
