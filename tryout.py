from swarm import Swarm, Agent
import os

os.environ['SWARM_DEFAULT_MODEL'] ='llama3.2:1b'
os.environ['OPENAI_ENDPOINT'] = 'http://localhost:11434/v1'
os.environ['OPENAI_API_KEY'] = 'blah'

client = Swarm()

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
)

french_agent = Agent(
    name="French Agent",
    instructions="You only speak French.",
)


def transfer_to_french_agent():
    """Transfer french speaking users immediately."""
    return french_agent


english_agent.functions.append(transfer_to_french_agent)

messages = [{"role": "user", "content": "Bonjour, Comment-allez vous?"}]
response = client.run(agent=english_agent, messages=messages)

print(response.messages[-1]["content"])
