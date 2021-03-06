from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json
import jsonify

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is empty!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('home.html', user=current_user)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})

@views.route('/delete-user', methods=['POST'])
@login_required
def delete_user():
    data = json.loads(request.data)
    userId = data['userId']
    user = User.query.get(userId)
    if user:
        if user.id == current_user.id:
            db.session.delete(user)
            db.session.commit()
            return 'Account Deleted!'