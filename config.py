import random
from openai import OpenAI
from keys import *

# Server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Models
local_mistral_8x7b = [
        {
            "model": "cjpais/llava-1.6-mistral-7b-gguf/llava-1.6-mistral-7b.Q6_K.gguf",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
        }
]

westlake = [
        {
            "model": "TheBloke/WestLake-7B-v2-GGUF",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
            "cache_seed": random.randint(0, 100000),
        }
]

gpt4_turbo = [{
        "model": "gpt-4-turbo-preview",
        "api_key": OPENAI_API_KEY,
        "cache_seed": random.randint(0, 100000),
}]

command_r = [
        {
            "model": "andrewcanis/c4ai-command-r-v01-GGUF",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
            "cache_seed": random.randint(0, 100000),
        }
]

llama3 = [
        {
            "model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
            'api_key': 'any string here is fine',
            'api_type': 'openai',
            'base_url': "http://localhost:1234/v1",
            "cache_seed": random.randint(0, 100000),
        }
]

