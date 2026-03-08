import os
from agents.extensions.models.litellm_model import LitellmModel

llm_model = LitellmModel(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openrouter/openai/gpt-5.2",
)
