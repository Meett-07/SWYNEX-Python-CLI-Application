import datetime
from typing import List, Dict
from storage import load_tasks, save_tasks
from exceptions import TaskNotFoundError, InvalidTaskDataError


def add_task(title: str) -> Dict:
    clean_title = title.strip()
    if not clean_title:
        raise InvalidTaskDataError("Task title cannot be empty.")

    tasks = load_tasks()

    if not tasks:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1

    new_task = {
        "id": new_id,
        "title": clean_title,
        "status": "pending",
        "created_at": datetime.datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task


def list_tasks() -> List[Dict]:
    return load_tasks()


def delete_task(task_id: int) -> None:
    tasks = load_tasks()

    task_exists = any(task["id"] == task_id for task in tasks)

    if not task_exists:
        raise TaskNotFoundError(task_id)

    updated_tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(updated_tasks)


if __name__ == "__main__":
    # Test adding tasks
    task1 = add_task("Learn Python Architecture")
    task2 = add_task("Build Make.com Integrations")
    print(f"Added tasks: {task1['id']} and {task2['id']}")
    
    # Test listing tasks
    all_tasks = list_tasks()
    print(f"Total tasks in database: {len(all_tasks)}")
    
    # Test deleting a task
    delete_task(task1['id'])
    print("Deleted task 1 successfully.")
    
    # Test the exception handling (Uncomment the line below to see the custom error)
    # delete_task(999)