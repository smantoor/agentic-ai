from agent import TaskAgent
from task_store import TaskStore
from task_tools import TaskToolRegistry

store = TaskStore()
tools = TaskToolRegistry(store)
agent = TaskAgent(tools)

print(agent.run("List all my tasks"))
print(agent.run("Add 'Complete Prompt Engineering exercise’ for Friday as pending"))