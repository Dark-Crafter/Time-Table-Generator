from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    from .routes.timetable_routes import timetable_bp
    from .routes.teacher_routes import teacher_bp
    from .routes.course_routes import course_bp
    
    app.register_blueprint(timetable_bp)
    app.register_blueprint(teacher_bp)
    app.register_blueprint(course_bp)
    
    return app
