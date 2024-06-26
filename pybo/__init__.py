from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData               # 추가

naming_convention = {                           # 추가
    'ix' : 'ix_%(column_0_label)s',
    'uq' : 'uq_%(table_name)s_%(column_0_name)s',
    'ck' : "ck_%(table_name)s_%(column_0_name)s",
    "fk" : "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk" : "pk_%(table_name)s"
}


# db = SQLAlchemy()
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))   # 추가
migrate = Migrate()

def page_not_found(e):
    return render_template("404.html"), 404

def create_app():
    app = Flask(__name__)
    app.config.from_envvar("APP_CONFIG_FILE")  # 환경변수 설정으로 수정

    db.init_app(app)
    # migrate.init_app(app, db)
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):   # 추가
        migrate.init_app(app, db, render_as_batch=True)               # 추가
    else:
        migrate.init_app(app, db)

    from . import models

    from .views import main_views, test_views, question_views, answer_views
    from .views import auth_views, weather_views, graph_views, covid19_views
    from .filter import datetime_fmt

    app.register_blueprint(main_views.bp)
    app.register_blueprint(test_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(weather_views.bp)
    app.register_blueprint(graph_views.bp)
    app.register_blueprint(covid19_views.bp)
    app.jinja_env.filters['datetime'] = datetime_fmt
    
    app.register_error_handler(404, page_not_found)

    return app






