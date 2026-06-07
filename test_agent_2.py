import sys, os
os.environ.pop("OPENAI_API_KEY", None)
os.environ["CUSTOM_API_KEY"] = "sk-CUSTOM123"
sys.path.insert(0, "/home/mspbots/.hermes/hermes-agent")
from run_agent import AIAgent
agent = AIAgent(provider="custom", base_url="https://aigateway-sandbox.mspbots.ai/v1", model="gemini-3.1-pro-preview")
print("Agent api_key:", getattr(agent, "api_key", None))
