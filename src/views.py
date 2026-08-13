from flask import render_template, abort
from models import courses

def index():
    return render_template('index.html')

def course(course_id):
    index = course_id - 1
    if not (0 <= index < len(courses)):
        abort(404)
    return render_template('course.html', course=courses[index])