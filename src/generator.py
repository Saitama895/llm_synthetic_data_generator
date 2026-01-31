import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from src.prompts import instruction_response_prompt

# We are using groq's api key

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

groq = OpenAI(base_url = "https://api.groq.com/openai/v1", api_key = groq_api_key)

def generate_synthetic_data(
        domain: str,
        n_samples:  int,
        model : str = "llama-3.3-70b-versatile"):
    
    prompt = instruction_response_prompt(domain, n_samples)

    response = groq.chat.completions.create(
        model= model,
        messages= [{"role": "user", "content": prompt}],
        temperature= 0.6,
        presence_penalty=0.4,
        frequency_penalty=0.3
    )

    return json.loads(response.choices[0].message.content)
