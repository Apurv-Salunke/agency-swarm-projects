from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List

class RedundancyCheckTool(BaseTool):
    """
    This tool will assist the QualityAssuranceAgent in checking for redundancy in the drafted content,
    identifying repeated information or phrases.
    """

    drafted_content: Dict[str, str] = Field(
        ..., description="A dictionary containing drafted content with titles as keys and content as values."
    )
    redundancy_report: Dict[str, List[str]] = Field(
        ..., description="A dictionary to store redundancy findings for each piece of drafted content, with titles as keys."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will check for redundancy in the drafted content and identify repeated information or phrases.
        """
        redundancy_results = {}
        for title, content in self.drafted_content.items():
            # Simulate checking for redundancy
            phrases = content.split()
            seen = set()
            duplicates = set()
            for phrase in phrases:
                if phrase in seen:
                    duplicates.add(phrase)
                seen.add(phrase)
            self.redundancy_report[title] = list(duplicates)
            redundancy_results[title] = {
                "Drafted Content": content,
                "Redundant Phrases": list(duplicates)
            }

        # Return the redundancy check results
        return f"Redundancy Check Results: {redundancy_results}"