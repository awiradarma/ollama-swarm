from swarm import Swarm, Agent
import os

os.environ['SWARM_DEFAULT_MODEL'] ='llama3.2:1b'
os.environ['OPENAI_ENDPOINT'] = 'http://localhost:11434/v1'
os.environ['OPENAI_API_KEY'] = 'blah'

client = Swarm()

waiter_agent = Agent(
    name="Waiter Agent",
    instructions="You are a helpful agent that's acting as a waiter for a restaurant. Do not make up list of dishes. Only provide the list of dishes and their prices from the get_menu function.",
)

def get_menu(**kwargs) -> str:
    return "{'menu':[{'dishname':'Lasagna with meat ball','price':'$20'},{'dishname':'Cheese Pizza','price':'$12'}]}"

waiter_agent.functions.append(get_menu)

#messages = [{"role": "user", "content": "Hello, I'd like to order something to eat. What do you have?"}]
#response = client.run(agent=waiter_agent, messages=messages)

#print(response.messages[-1]["content"])

def pretty_print_messages(messages):
    for message in messages:
        if message["content"] is None:
            continue
        print(f"{message['sender']}: {message['content']}")


messages = []
while True:
    user_input = input("> ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(agent=waiter_agent, messages=messages)
    print(response.messages[-1]["content"])

    messages = response.messages
    agent = response.agent
    #pretty_print_messages(messages)