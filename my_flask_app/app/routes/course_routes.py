from flask import Blueprint, request, jsonify
from .. import db
from ..models import Course

course_bp = Blueprint('course_bp', __name__)

@course_bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses])

@course_bp.route('/courses', methods=['POST'])
def add_course():
    data = request.get_json()
    new_course = Course(
        name=data['name'],
        teacher_id=data['teacher_id']
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify(new_course.to_dict()), 201

@course_bp.route('/courses/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return '', 204

# Helper method to convert Course to dictionary
def course_to_dict(course):
    return {
        'id': course.id,
        'name': course.name,
        'teacher_id': course.teacher_id
    }

Course.to_dict = course_to_dict
