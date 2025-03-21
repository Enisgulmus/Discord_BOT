import sys
import os
from database import add_task_id, complete_task_id, get_all_tasks

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_complete_task():
    description = "Tamamlanacak görev"
    add_task_id(description)
    tasks = get_all_tasks()
    task_id = next(task[0] for task in tasks if task[1] == description)
    complete_task_id(task_id)
    updated_tasks = get_all_tasks()
    assert any(task[0] == task_id and task[2] == 1 for task in updated_tasks)
