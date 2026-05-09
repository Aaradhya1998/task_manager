from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

# PostgreSQL integration: this SQLAlchemy instance is initialized by app.py.
db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)

    tasks = db.relationship(
        'Task',
        backref='user',
        lazy=True,
        cascade='all, delete-orphan'
    )


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text)

    priority = db.Column(db.String(20), default='Medium')

    status = db.Column(db.String(20), default='Pending')

    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def created_at(self):
        """Backward-compatible alias for existing templates/API code."""
        return self.created_date
