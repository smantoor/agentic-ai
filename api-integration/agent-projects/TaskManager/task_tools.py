import json
import task_store

class TaskToolRegistry:

    def __init__(self,store):
        self.store = store


    @property
    def schemas(self) -> list[dict]:
        return [
            {
                "type":"function",
                "name":"list_tasks",
                "description":"Lists all tasks",
                "parameters":{
                    "type":"object",
                    "properties":{}
                },
            },
            {
                "type": "function",
                "name": "add_task",
                "description": "Create a new task with an optional due date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "Short task title"
                        },
                        "due_date": {
                            "type": "string",
                            "description": "Optional due date, for example Friday"
                        },
                        "status":{
                            "type": "string",
                            "description":"Add the task status"
                        }
                    }
                }
            }    
        ]

    def execute(self, name:str, arguments:str):
        if name == "list_tasks":
            return self.store.list_tasks()
        if name == "add_task":
            args = json.loads(arguments)
            print(args)
            print((args['title'],args['due_date'], args['status']))
            return self.store.add_task(args['title'],args['due_date'], args['status'])