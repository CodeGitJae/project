from config.default import *

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
        os.path.join(BASE_DIR, 'pybo.db')
)

SQLALCHEMY_TRACK_MODIFICATIONS=False


SECRET_KEY=b'\xc9\xa5SF\xd1\xeb\xf4\x8d_\xf1\xc2\xb1a8\xcc\x1f'