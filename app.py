from flask import Flask
from flask import render_template
from flask_login import LoginManager, current_user, login_required
from flask_socketio import SocketIO

from config import Config
from analytics.analytics import generate_task_analytics
from models.models import db, Task, User
from routes.auth import init_auth_routes
from routes.tasks import init_task_routes


app = Flask(__name__)
app.config.from_object(Config)

# PostgreSQL integration: bind the shared SQLAlchemy instance to this Flask app.
db.init_app(app)

socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


init_auth_routes(app)
init_task_routes(app, socketio)


@app.route('/')
def home():
    return "Smart Task Manager Running"


@app.route('/dashboard')
@login_required
def dashboard():

    tasks = Task.query.filter_by(
        user_id=current_user.id
    ).all()

    analytics = generate_task_analytics(
        current_user.id
    )

    return render_template(
        'dashboard.html',
        tasks=tasks,
        analytics=analytics
    )


# PostgreSQL integration: create the configured database tables on startup.
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    socketio.run(app, debug=True)
