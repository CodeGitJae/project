from config.default import *
from logging.config import dictConfig

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:1@localhost:3306/flask_db".format(
        os.path.join(BASE_DIR, 'pybo.db')
)

SQLALCHEMY_TRACK_MODIFICATIONS=False


SECRET_KEY=b'\xc9\xa5SF\xd1\xeb\xf4\x8d_\xf1\xc2\xb1a8\xcc\x1f'

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format" : "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "file":{
                "level": "INFO",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(BASE_DIR, "logs/project.log"),
                "maxBytes": 1024 * 1024 * 5, # 5MB
                "backupCount": 5,
                "formatter": "default",
            },
        },
        "root": {
            "level": "INFO", # debug -> info -> warning -> error -> critical
            "handlers": ["file"]
        }

    })