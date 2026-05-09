import pandas as pd
import numpy as np

from models.models import Task


def generate_task_analytics(user_id):

    tasks = Task.query.filter_by(user_id=user_id).all()

    if not tasks:

        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_rate": 0
        }

    task_data = []

    for task in tasks:

        task_data.append({
            "title": task.title,
            "status": task.status
        })

    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    completed_tasks = len(
        df[df['status'] == 'Completed']
    )

    pending_tasks = len(
        df[df['status'] == 'Pending']
    )

    completion_rate = np.round(
        (completed_tasks / total_tasks) * 100,
        2
    )

    return {
        "total_tasks": int(total_tasks),
        "completed_tasks": int(completed_tasks),
        "pending_tasks": int(pending_tasks),
        "completion_rate": float(completion_rate)
    }