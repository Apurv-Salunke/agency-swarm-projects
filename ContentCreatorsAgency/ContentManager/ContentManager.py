from agency_swarm.agents import Agent


class ContentManager(Agent):
    def __init__(self):
        super().__init__(
            name="ContentManager",
            description="This agent serves as the entry point for communication with the user, handling user interactions and coordinating the content creation process.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
