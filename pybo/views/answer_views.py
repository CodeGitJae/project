from flask import Flask, Blueprint, render_template, request, url_for, flash, g
from pybo.models import Question, Answer
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect
from pybo.forms import AnswerForm
from pybo.views.auth_views import required_login
from flask_wtf import FlaskForm  

bp = Blueprint("answer", __name__, url_prefix="/answer")

@bp.route("/delete/<int:answer_id>")
@required_login
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id  # return 시  lazy loading 오류가 발생하기 때문에 코드 실행 전에 question_id를 선언해주고 시작

    if g.user != answer.user:
        flash("삭제 권한이 없습니다.")   # 코드 실행 후 페이지 이동이 없기 때문에 return 값을 넣지 않았음.
    
    else:
        db.session.delete(answer)
        db.session.commit()

    return redirect(url_for("question.detail", question_id=question_id))


@bp.route("/update/<int:answer_id>", methods=("GET","POST")) # href값 입력할 때 answer_id 변수 선언함
@required_login
def update(answer_id):
    answer = Answer.query.get_or_404(answer_id)

    if g.user != answer.user:
        flash("수정 권한이 없습니다.")
        return redirect(url_for("question.detail", question_id=answer.question.id))

    if request.method =="GET":
        form = AnswerForm(obj=answer)
    else:
        form = AnswerForm()    # "POST" 전송 방식일 떄 받는 값
        if form.validate_on_submit():
            form.populate_obj(answer)  # populate 뜻은 이주시키다. from 값을 answer에 넣는다는 뜻
            answer.update_date = datetime.now()
            db.session.commit()
            return redirect(url_for('question.detail', question_id=answer.question.id))

    return render_template('answer/answer_form.html', form=form)

@bp.route("/create/<int:question_id>", methods=("POST","GET"))
@required_login
def create(question_id):

    form = AnswerForm()

    question = Question.query.get_or_404(question_id)

    if request.method == 'POST' and form.validate_on_submit():
        content = request.form["content"]
        create_date = datetime.now()
        user_id = request.form["user_id"]   # 추가
        answer = Answer(question=question, content=content, create_date=create_date, user_id=user_id) # 추가
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for("question.detail", question_id=question.id))

    return render_template("question/question_detail.html", question=question, form=form)