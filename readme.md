# Python CLI Task Manager

A modular command-line task manager built to demonstrate production-ready Python architecture.

## Architecture
- **cli.py:** Handles user input parsing via `argparse`.
- **core.py:** Contains business logic and state management.
- **storage.py:** Manages File I/O for JSON serialization.
- **exceptions.py:** Defines custom domain errors for clean exception handling.

## Usage
`python main.py add "Task Name"`
`python main.py list`
`python main.py delete <id>`