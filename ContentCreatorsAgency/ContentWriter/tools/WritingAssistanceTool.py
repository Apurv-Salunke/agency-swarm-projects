from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class WritingAssistanceTool(BaseTool):
    """
    This tool will assist the ContentWriter in drafting content by providing writing prompts,
    suggestions, and structure based on the outlines provided by the ContentPlanner.
    """

    outlines: Dict[str, List[str]] = Field(
        ..., description="A dictionary containing structured outlines for content, with topics as keys and outlines as values."
    )
    writing_prompts: Dict[str, str] = Field(
        ..., description="A dictionary to store writing prompts for each topic, with topics as keys."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will provide writing prompts and suggestions based on the outlines.
        """
        writing_assistance = {}
        for topic, outline in self.outlines.items():
            # Simulate generating writing prompts based on the outline
            prompt = f"Draft content for the topic '{topic}' using the following structure: {outline}"
            self.writing_prompts[topic] = prompt
            writing_assistance[topic] = {
                "Outline": outline,
                "Writing Prompt": prompt
            }

        # Return the writing assistance information
        return f"Writing Assistance: {writing_assistance}"