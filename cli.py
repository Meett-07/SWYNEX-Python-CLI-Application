import argparse
from core import add_task, list_tasks, delete_task
from exceptions import TaskException, TaskManagerError


def main():
    # 1. Initialize the root parser
    parser = argparse.ArgumentParser(
        prog="task_manager",
        description="A robust CLI Task Manager."
    )
    
    # 2. Set up subcommands (e.g., 'add', 'list', 'delete')
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # --- SUBCOMMAND: add ---
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="The title of the task")
    
    # --- SUBCOMMAND: list ---
    # The list command requires no arguments, so we just declare it
    list_parser = subparsers.add_parser("list", help="List all pending tasks")
    
    # --- SUBCOMMAND: delete ---
    delete_parser = subparsers.add_parser("delete", help="Delete a task by ID")
    delete_parser.add_argument("id", type=int, help="The numeric ID of the task to delete")

    # 3. Parse the arguments typed in the terminal
    args = parser.parse_args()

    # 4. Route the command to the correct core logic
    try:
        if args.command == "add":
            task = add_task(args.title)
            print(f"Success: Added task [{task['id']}] '{task['title']}'")
            
        elif args.command == "list":
            tasks = list_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nCURRENT TASKS:")
                for t in tasks:
                    created_at = t.get("created_at", "")[:10] if t.get("created_at") else "N/A"
                    print(f"[{t['id']}] {t.get('title', 'Untitled')} (Added: {created_at})")
                print("-" * 20)
                
        elif args.command == "delete":
            delete_task(args.id)
            print(f"Success: Task ID {args.id} deleted.")
            
        else:
            # If the user types 'python cli.py' with no command, show the help menu
            parser.print_help()

    # 5. The safety net: Catching our custom domain errors
    except (TaskException, TaskManagerError) as e:
        print(f"\nERROR: {e}\n")


if __name__ == "__main__":
    main()