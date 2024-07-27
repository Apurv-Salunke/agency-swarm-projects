from agency_swarm.agents import Agent


class ContentWriter(Agent):
    def __init__(self):
        super().__init__(
            name="ContentWriter",
            description="A Content Writer agent responsible for creating well-structured drafts based on the outline provided by the Content Strategist using internal capabilities for text generation with effective prompting.",
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
