import json
from pathlib import Path

# Task store does tasks operation like listing tasks, adding and updating task using tasks.json file
class TaskStore:

    def __init__(self,jsonFile="tasks.json"):
            """
            Initializes the TaskStore instance and resolves the file path.
                Args:
            jsonFile (str): The filename/relative path of the JSON file storing tasks.
            """
            base_dir = Path(__file__).parent.resolve()
            self.jsonFile = base_dir/jsonFile

    def list_tasks(self)->list:
            """
            Reads and parses task data from the target JSON file.
            Returns:
            dict or list: The parsed JSON contents representing existing tasks.
            """            
            try:
                print(self.jsonFile)
                with open(self.jsonFile,"r") as fRead:
                    data = json.load(fRead)
                    print(data)
                    return data
            except Exception as e:
                raise e
                return []

    def new_task_schema(self,id:int,title:str, due_date:str, status:str)->str:
        """
        Constructs a dictionary matching the standard schema for a single task entry.
        
        Args:
            id (int): Unique identifier for the task.
            title (str): Title or summary of the task.
            due_date (str): Expected completion date (e.g., 'YYYY-MM-DD').
            status (str): Current execution state (e.g., 'Pending', 'Completed').
            
        Returns:
            dict: Structured dictionary representing a new task object.
        """
        new_task={
            "id": id,
            "title": title,
            "due_date": due_date,
            "status": status
        }
        return new_task

    def add_task(self, title:str, due_date:str, status:str)->None:
            """
            Creates a new task with an auto-incremented ID and appends it to the JSON store.
        
            Args:
            title (str): Title of the new task.
            due_date (str): Target due date for the task.
            status (str): Initial status of the task.
            """
            # Fetch existing data from the storage file
            data = self.list_tasks()
            tasks = data['tasks']

            # Iterate through existing tasks to reach the last entry
            # NOTE: If 'tasks' is empty, 'task' won't be assigned, raising an UnboundLocalError below.
            for task in tasks:
                  pass
            latest_id = int(task['id'])+1
            json_new_task = self.new_task_schema(latest_id,title, due_date, status)
            tasks.append(json_new_task)
            try:
                with open(self.jsonFile,"w") as fWrite:
                    json.dump(tasks, fWrite, indent=2)
            except Exception as e:
                print("File writing failed")
                raise(e)

    def update_task(self,task:list,status:str)->None:
         pass


