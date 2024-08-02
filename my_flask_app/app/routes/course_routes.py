from flask import Blueprint, jsonify, request
from app.models import db, Course

course_bp = Blueprint('course', __name__, url_prefix='/course')

@course_bp.route('/', methods=['GET'])
def get_courses():
    # Implement logic to get courses
    return jsonify([])  # Replace with actual data

@course_bp.route('/<int:id>', methods=['GET'])
def get_course(id):
    # Implement logic to get a single course by ID
    return jsonify({})  # Replace with actual data
