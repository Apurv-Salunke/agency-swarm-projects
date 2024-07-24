from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict

class FeedbackProvisionTool(BaseTool):
    """
    This tool will facilitate the provision of feedback to the ContentWriter and ContentManager
    based on the quality evaluation results.
    """

    evaluation_results: Dict[str, str] = Field(
        ..., description="A dictionary containing evaluation results for each piece of content, with titles as keys."
    )
    feedback_messages: Dict[str, str] = Field(
        ..., description="A dictionary to store feedback messages for each piece of content, with titles as keys."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method will generate feedback based on the quality evaluation results.
        """
        feedback_summary = {}
        for title, result in self.evaluation_results.items():
            # Simulate generating feedback based on evaluation results
            if "scored 0" in result:
                feedback = f"Content '{title}' needs significant improvement. Please revise the content."
            elif "scored 1" in result:
                feedback = f"Content '{title}' meets some criteria but requires further refinement."
            elif "scored" in result:
                feedback = f"Content '{title}' is satisfactory. Good job!"
            else:
                feedback = f"Content '{title}' evaluation is inconclusive."

            self.feedback_messages[title] = feedback
            feedback_summary[title] = {
                "Evaluation Result": result,
                "Feedback": feedback
            }

        # Return the feedback results
        return f"Feedback Provision Results: {feedback_summary}"