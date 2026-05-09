from flask import jsonify, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models.models import db, Task


def init_task_routes(app, socketio):

    @app.route('/tasks/add', methods=['POST'])
    @login_required
    def add_task():

        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority')

        new_task = Task(
            title=title,
            description=description,
            priority=priority,
            user_id=current_user.id
        )

        # PostgreSQL integration: persist task changes through SQLAlchemy sessions.
        db.session.add(new_task)
        db.session.commit()

        socketio.emit('task_added', {
            'message': f'New task added: {title}'
        })

        flash('Task added successfully')

        return redirect(url_for('dashboard'))


    @app.route('/tasks/update/<int:id>', methods=['POST'])
    @login_required
    def update_task(id):

        task = db.get_or_404(Task, id)

        if task.user_id != current_user.id:
            flash('Unauthorized access')
            return redirect(url_for('dashboard'))

        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.priority = request.form.get('priority')
        task.status = request.form.get('status')

        db.session.commit()

        socketio.emit('task_updated', {
            'message': f'Task updated: {task.title}'
        })

        flash('Task updated successfully')

        return redirect(url_for('dashboard'))


    @app.route('/tasks/delete/<int:id>')
    @login_required
    def delete_task(id):

        task = db.get_or_404(Task, id)

        if task.user_id != current_user.id:
            flash('Unauthorized access')
            return redirect(url_for('dashboard'))

        db.session.delete(task)
        db.session.commit()

        socketio.emit('task_deleted', {
            'message': f'Task deleted'
        })

        flash('Task deleted successfully')

        return redirect(url_for('dashboard'))


    @app.route('/api/tasks', methods=['GET'])
    @login_required
    def get_tasks_api():

        tasks = Task.query.filter_by(
            user_id=current_user.id
        ).all()

        task_list = []

        for task in tasks:

            task_list.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "status": task.status,
                "created_date": task.created_date.strftime('%Y-%m-%d'),
                "created_at": task.created_date.strftime('%Y-%m-%d')
            })

        return jsonify({
            "success": True,
            "tasks": task_list
        })


    @app.route('/api/tasks/add', methods=['POST'])
    @login_required
    def add_task_api():

        data = request.get_json()

        new_task = Task(
            title=data.get('title'),
            description=data.get('description'),
            priority=data.get('priority'),
            status='Pending',
            user_id=current_user.id
        )

        db.session.add(new_task)
        db.session.commit()

        socketio.emit('task_added', {
            'message': f'New task added: {new_task.title}'
        })

        return jsonify({
            "success": True,
            "message": "Task added successfully"
        })


    @app.route('/api/tasks/update/<int:id>', methods=['PUT'])
    @login_required
    def update_task_api(id):

        task = db.get_or_404(Task, id)

        if task.user_id != current_user.id:

            return jsonify({
                "success": False,
                "message": "Unauthorized"
            }), 403

        data = request.get_json()

        task.title = data.get('title', task.title)

        task.description = data.get(
            'description',
            task.description
        )

        task.priority = data.get(
            'priority',
            task.priority
        )

        task.status = data.get(
            'status',
            task.status
        )

        db.session.commit()

        socketio.emit('task_updated', {
            'message': f'Task updated: {task.title}'
        })

        return jsonify({
            "success": True,
            "message": "Task updated successfully"
        })


    @app.route('/api/tasks/delete/<int:id>', methods=['DELETE'])
    @login_required
    def delete_task_api(id):

        task = db.get_or_404(Task, id)

        if task.user_id != current_user.id:

            return jsonify({
                "success": False,
                "message": "Unauthorized"
            }), 403

        db.session.delete(task)

        db.session.commit()

        socketio.emit('task_deleted', {
            'message': 'Task deleted'
        })

        return jsonify({
            "success": True,
            "message": "Task deleted successfully"
        })
