from agency_swarm.agents import Agent


class ClientRelationsManager(Agent):
    def __init__(self):
        super().__init__(
            name="ClientRelationsManager",
            description="A Client Relations Manager agent responsible for managing client communication and submitting the final draft for approval.",
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
