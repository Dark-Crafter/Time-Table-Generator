from flask import Blueprint, request, jsonify
from .. import db
from ..models import Teacher

teacher_bp = Blueprint('teacher_bp', __name__)

@teacher_bp.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    return jsonify([t.to_dict() for t in teachers])

@teacher_bp.route('/teachers', methods=['POST'])
def add_teacher():
    data = request.get_json()
    new_teacher = Teacher(
        name=data['name'],
        max_hours_per_day=data.get('max_hours_per_day', 3),
        max_hours_per_week=data.get('max_hours_per_week', 40)
    )
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify(new_teacher.to_dict()), 201

@teacher_bp.route('/teachers/<int:id>', methods=['DELETE'])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    return '', 204

# Helper method to convert Teacher to dictionary
def teacher_to_dict(teacher):
    return {
        'id': teacher.id,
        'name': teacher.name,
        'max_hours_per_day': teacher.max_hours_per_day,
        'max_hours_per_week': teacher.max_hours_per_week
    }

Teacher.to_dict = teacher_to_dict
