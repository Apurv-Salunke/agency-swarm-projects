from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class ResearchTool(BaseTool):
    """
    This tool will assist the ContentPlanner in conducting research on specified topics,
    gathering relevant information, and summarizing findings for content planning.
    """

    topics: List[str] = Field(
        ..., description="A list of topics to research for content planning."
    )
    research_results: Dict[str, str] = Field(
        ..., description="A dictionary to store the research findings, with topics as keys and their summaries as values."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will conduct research on the specified topics and summarize the findings.
        """
        for topic in self.topics:
            # Simulate a research process
            self.research_results[topic] = f"Summary of findings for {topic}"

        # Return the research results
        return f"Research Results: {self.research_results}"