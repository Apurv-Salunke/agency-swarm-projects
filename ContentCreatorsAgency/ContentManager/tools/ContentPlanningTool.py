from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class ContentPlanningTool(BaseTool):
    """
    This tool will assist the ContentManager in creating structured content plans,
    including defining topics, target audience, and timelines for content production.
    """

    topics: List[str] = Field(
        ..., description="A list of topics to be covered in the content plan."
    )
    target_audience: str = Field(
        ..., description="The target audience for the content."
    )
    timeline: Dict[str, str] = Field(
        ..., description="A dictionary defining the timeline for content production, with keys as milestones and values as dates."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will create a structured content plan based on the provided topics, target audience, and timeline.
        """
        content_plan = {
            "topics": self.topics,
            "target_audience": self.target_audience,
            "timeline": self.timeline
        }

        # Return the structured content plan as a string
        return f"Content Plan Created: {content_plan}"