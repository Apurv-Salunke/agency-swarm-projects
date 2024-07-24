from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class ResearchCollaborationTool(BaseTool):
    """
    This tool will enable the ContentWriter to conduct research on specific topics
    and collaborate with the ContentPlanner for gathering relevant information.
    """

    topics: List[str] = Field(
        ..., description="A list of topics for which research will be conducted."
    )
    research_results: Dict[str, str] = Field(
        ..., description="A dictionary to store research findings for each topic, with topics as keys."
    )
    collaboration_notes: Dict[str, str] = Field(
        ..., description="A dictionary to store notes from collaboration with the ContentPlanner, with topics as keys."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will conduct research on specified topics and gather relevant information.
        """
        collaboration_info = {}
        for topic in self.topics:
            # Simulate conducting research and collaboration
            research_findings = f"Research findings for {topic} gathered successfully."
            collaboration_note = f"Collaborated with ContentPlanner on {topic}."
            self.research_results[topic] = research_findings
            self.collaboration_notes[topic] = collaboration_note
            collaboration_info[topic] = {
                "Research Findings": research_findings,
                "Collaboration Note": collaboration_note
            }

        # Return the collaboration and research information
        return f"Research Collaboration Results: {collaboration_info}"