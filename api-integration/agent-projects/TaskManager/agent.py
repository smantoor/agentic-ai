import json
import task_store
import task_tools
from openai import OpenAI
from dotenv import load_dotenv

class TaskAgent:

    def __init__(self, tool_registry):
        load_dotenv()
        self.client = OpenAI()
        self.tools = tool_registry
        self.model = "gpt-4o-mini"

    def run(self, user_message:str):
        input_items = [{"role":"user", "content":user_message}]

        for _ in range(5):
            response = self.client.responses.create(
                model = self.model,
                tools = self.tools.schemas,
                input = input_items,
            )

            input_items.extend(response.output)

            has_tool_call = False

            for item in response.output:
                if item.type == "function_call":
                    has_tool_call = True
                    result = self.tools.execute(item.name, item.arguments)
                    input_items.append(
                        {
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": json.dumps(result),
                        }
                    )
                if not has_tool_call:
                    return response.output_text
        return "Unable to complete the request after several tool calls."


