from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timetable.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .routes.timetable_routes import timetable_bp
from .routes.teacher_routes import teacher_bp
from .routes.course_routes import course_bp

app.register_blueprint(timetable_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(course_bp)

def create_tables():
    db.create_all()
