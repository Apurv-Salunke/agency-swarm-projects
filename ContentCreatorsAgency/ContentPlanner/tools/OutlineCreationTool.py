from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class OutlineCreationTool(BaseTool):
    """
    This tool will enable the ContentPlanner to create structured outlines for content
    based on the research findings and defined topics.
    """

    topics: List[str] = Field(
        ..., description="A list of topics for which structured outlines will be created."
    )
    research_findings: Dict[str, str] = Field(
        ..., description="A dictionary containing research findings, with topics as keys and their summaries as values."
    )
    outlines: Dict[str, List[str]] = Field(
        ..., description="A dictionary to store the structured outlines for each topic, with topics as keys and outlines as values."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will create structured outlines for content based on the research findings.
        """
        for topic in self.topics:
            if topic in self.research_findings:
                # Simulate outline creation based on research findings
                self.outlines[topic] = [
                    f"Introduction to {topic}",
                    f"Key Points from Research: {self.research_findings[topic]}",
                    f"Conclusion on {topic}"
                ]
            else:
                self.outlines[topic] = ["No research findings available for this topic."]

        # Return the created outlines
        return f"Created Outlines: {self.outlines}"