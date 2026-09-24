import json
from typing import List,Dict
FILE_NAME="tasks.json"
def load_tasks()->List[Dict]:
    try:
        with open(FILE_NAME,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return []
def save_tasks(tasks:List[Dict])->None:
    with open(FILE_NAME,'w') as file:
        json.dump(tasks,file,indent=4)

if __name__ == "__main__":
    # 1. Create a dummy task
    dummy_data = [{"id": 1, "title": "Master Python File I/O", "status": "pending"}]
    
    # 2. Save it
    save_tasks(dummy_data)
    print("Task saved. Check your folder for tasks.json.")
    
    # 3. Load it back
    loaded_data = load_tasks()
    print(f"Data loaded from file: {loaded_data}")
