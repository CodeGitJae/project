from flask import Flask, Blueprint, render_template

bp = Blueprint("covid19", __name__, url_prefix="/covid19")


@bp.route("/vaccin")
def vaccin():
    return render_template("covid19/covid_prs.html")

@bp.route("/covid19category")
def covid19_category():

    form = [
        {
        "title" : "코로나19 예방 접종 현황",
        "content" : "코로나19 예방접종으로 중증화 예방효과 및 변이 바이러스 출현으로 인한 중증도가 증가 억제 백신접종을 통해 중증 진행을 예방",
        "img": "/upload/vaccinimg.jpg",
        "href" : "covid19.vaccin"
    },
    {
        "title" : "서울시 코로나19 확진자 전수 조사 현황",
        'content': "2020년 ~ 2023년 5월까지 서울시에서 발생한 코로나19 확진자, 완치자, 사망자 수를 직관적으로 볼수 있게 그래프를 통해 가시화",
        "img": "/upload/covid19img.jpg",
        "href" : "graph.covid19_analysis"
    }
    ]

    return render_template("covid19/covid19_inform.html", form=form)