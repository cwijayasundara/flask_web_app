from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8u3rouhfkjdsfiluh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from routes import *


def create_app():
    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
