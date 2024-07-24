from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict
from datetime import datetime

class SchedulingTool(BaseTool):
    """
    This tool will support the ContentPlanner in scheduling content production tasks,
    including setting deadlines and reminders for the ContentManager and other agents.
    """

    tasks: List[str] = Field(
        ..., description="A list of content production tasks to be scheduled."
    )
    deadlines: Dict[str, datetime] = Field(
        ..., description="A dictionary to store deadlines for each task, with tasks as keys and their deadlines as values."
    )
    reminders: Dict[str, str] = Field(
        ..., description="A dictionary to store reminders for each task, with tasks as keys and their reminder messages as values."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will schedule content production tasks, setting deadlines and reminders.
        """
        scheduled_info = {}
        for task in self.tasks:
            # Simulate scheduling process
            deadline = datetime.now()  # Example: setting deadline to now for demonstration
            reminder = f"Reminder for task '{task}' is set."
            self.deadlines[task] = deadline
            self.reminders[task] = reminder
            scheduled_info[task] = {
                "Deadline": deadline,
                "Reminder": reminder
            }

        # Return the scheduled tasks information
        return f"Scheduled Tasks: {scheduled_info}"