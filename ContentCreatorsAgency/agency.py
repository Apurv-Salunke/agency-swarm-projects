from agency_swarm import Agency
from QualityAssuranceAgent import QualityAssuranceAgent
from ContentWriter import ContentWriter
from ContentPlanner import ContentPlanner
from ContentManager import ContentManager

content_manager = ContentManager()
content_planner = ContentPlanner()
content_writer = ContentWriter()
quality_assurance_agent = QualityAssuranceAgent()

agency = Agency([content_manager, [content_manager, content_planner],
                 [content_manager, content_writer],
                 [content_manager, quality_assurance_agent]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()