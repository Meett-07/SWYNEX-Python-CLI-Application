"""
Custom exceptions for the WYNEX Task Management CLI Application.
"""

from typing import Optional, List


class TaskException(Exception):
    """Base exception class for all task-related errors."""
    pass


# Alias for backward compatibility / domain naming
TaskManagerError = TaskException


class TaskNotFoundError(TaskException):
    """Raised when a task with the specified ID cannot be found."""

    def __init__(self, task_id: int, message: Optional[str] = None):
        self.task_id = task_id
        if message is None:
            message = f"Task with ID {task_id} was not found."
        super().__init__(message)


class InvalidTaskDataError(TaskException):
    """Raised when task input is invalid (e.g., empty title, invalid description)."""
    pass


class InvalidStatusError(TaskException):
    """Raised when an unsupported or invalid status is assigned to a task."""

    def __init__(self, status: str, valid_statuses: Optional[List[str]] = None, message: Optional[str] = None):
        self.status = status
        self.valid_statuses = valid_statuses
        if message is None:
            if valid_statuses:
                message = f"Invalid status '{status}'. Allowed statuses: {', '.join(valid_statuses)}."
            else:
                message = f"Invalid status '{status}'."
        super().__init__(message)


class StorageError(TaskException):
    """Raised when an error occurs while reading from or writing to storage."""
    pass
