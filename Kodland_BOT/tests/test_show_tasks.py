import sys
import os
from database import add_task_id, get_all_tasks

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_show_tasks():
    description = "Gösterilecek görev"
    add_task_id(description)
    tasks = get_all_tasks()
    assert any(task[1] == description for task in tasks)
