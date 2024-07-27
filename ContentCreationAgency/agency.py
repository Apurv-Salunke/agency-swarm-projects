from agency_swarm import Agency
from ContentEditor import ContentEditor
from ContentWriter import ContentWriter
from ClientRelationsManager import ClientRelationsManager
from ContentStrategist import ContentStrategist

ceo = ContentStrategist()
writer = ContentWriter()
editor = ContentEditor()
client_manager = ClientRelationsManager()

agency = Agency([ceo, client_manager, 
                 [ceo, writer],
                #  [writer, editor],
                 [editor, writer],
                 [client_manager, editor]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio(auth=("admin", "pass1234"))