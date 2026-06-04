"""Basic test suite for the task manager."""

import unittest
from task_manager import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    view_all_tasks,
    calculate_progress,
)
from task_manager import task_utils


class TaskManagerTests(unittest.TestCase):

    def setUp(self):
        task_utils.tasks.clear()

    def test_add_task(self):
        task = add_task("Plan", "Write a short plan.", "2099-01-01")
        self.assertEqual(task["id"], 1)
        self.assertFalse(task["completed"])
        self.assertEqual(len(view_all_tasks()), 1)

    def test_mark_task_as_complete(self):
        task = add_task("Test", "Run a test.", "2099-01-02")
        self.assertTrue(mark_task_as_complete(task["id"]))
        self.assertTrue(task["completed"])

    def test_view_pending_tasks(self):
        add_task("First", "Task one description.", "2099-01-03")
        add_task("Second", "Task two description.", "2099-01-04")
        mark_task_as_complete(1)
        pending = view_pending_tasks()
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0]["id"], 2)

    def test_calculate_progress(self):
        add_task("One", "Do this.", "2099-01-05")
        add_task("Two", "Do that.", "2099-01-06")
        mark_task_as_complete(2)
        progress = calculate_progress()
        self.assertEqual(progress["total_tasks"], 2)
        self.assertEqual(progress["completed_tasks"], 1)
        self.assertEqual(progress["pending_tasks"], 1)
        self.assertEqual(progress["completion_percentage"], 50.0)


if __name__ == "__main__":
    unittest.main()

