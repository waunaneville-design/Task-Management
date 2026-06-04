"""
Task Manager Package
A package for managing tasks and tracking progress.
"""

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    view_all_tasks,
    calculate_progress
)

__all__ = [
    'validate_task_title',
    'validate_task_description',
    'validate_due_date',
    'add_task',
    'mark_task_as_complete',
    'view_pending_tasks',
    'view_all_tasks',
    'calculate_progress'
]
