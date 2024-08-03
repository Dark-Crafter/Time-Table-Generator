from . import db

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    max_hours_per_day = db.Column(db.Integer, nullable=False, default=3)
    max_hours_per_week = db.Column(db.Integer, nullable=False, default=40)
    courses = db.relationship('Course', backref='teacher', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    timetable_entries = db.relationship('TimetableEntry', backref='course', lazy=True)

class TimetableEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(10), nullable=False)
    start_time = db.Column(db.String(5), nullable=False)
    end_time = db.Column(db.String(5), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
