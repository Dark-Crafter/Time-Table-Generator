from flask import Blueprint, request, jsonify
from .. import db
from ..models import TimetableEntry, Course

timetable_bp = Blueprint('timetable_bp', __name__)

@timetable_bp.route('/timetables', methods=['GET'])
def get_timetables():
    timetables = TimetableEntry.query.all()
    return jsonify([t.to_dict() for t in timetables])

@timetable_bp.route('/timetables', methods=['POST'])
def add_timetable_entry():
    data = request.get_json()
    new_entry = TimetableEntry(
        day_of_week=data['day_of_week'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        course_id=data['course_id']
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify(new_entry.to_dict()), 201

@timetable_bp.route('/timetables/<int:id>', methods=['DELETE'])
def delete_timetable_entry(id):
    entry = TimetableEntry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return '', 204

# Helper method to convert TimetableEntry to dictionary
def timetable_entry_to_dict(entry):
    return {
        'id': entry.id,
        'day_of_week': entry.day_of_week,
        'start_time': entry.start_time,
        'end_time': entry.end_time,
        'course_id': entry.course_id
    }

TimetableEntry.to_dict = timetable_entry_to_dict
