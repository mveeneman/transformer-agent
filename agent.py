import openai
import os
from helper import get_huggingface_api_key
from huggingface_hub import login, InferenceClient

login(get_huggingface_api_key())

from transformers import CodeAgent

client = InferenceClient(model="meta-llama/Meta-Llama-3-8B-Instruct")
    
def llm_engine(messages, stop_sequences=["Task"]) -> str:
    response = client.chat_completion(messages, stop=stop_sequences, max_tokens=1000)
    answer = response.choices[0].message.content
    return answer                     
                         
agent = CodeAgent(tools=[], llm_engine=llm_engine, add_base_tools=True)

agent.run(
    "Could you translate this sentence from French, say it out loud and return the audio.",
    sentence="Où est la boulangerie la plus proche?",
)

print(agent)