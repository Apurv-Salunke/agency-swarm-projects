from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class ContentWritingTool(BaseTool):
    """
    This tool will enable the ContentManager to facilitate the writing process by coordinating
    with the ContentWriter, including assigning tasks and tracking progress.
    """

    tasks: List[str] = Field(
        ..., description="A list of writing tasks to be assigned to the ContentWriter."
    )
    progress_tracking: Dict[str, str] = Field(
        ..., description="A dictionary to track the progress of each task, with task names as keys and their statuses as values."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will facilitate the writing process by assigning tasks and tracking their progress.
        """
        # Example of assigning tasks and tracking progress
        for task in self.tasks:
            self.progress_tracking[task] = "Assigned"

        # Return the current status of tasks and their progress
        return f"Tasks Assigned: {self.tasks}, Progress: {self.progress_tracking}"