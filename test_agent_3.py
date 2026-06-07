import sys, os
sys.path.insert(0, "/home/mspbots/.hermes/hermes-agent")

# Fake the hermes constants to use an empty profile dir
import tempfile
d = tempfile.mkdtemp()
with open(os.path.join(d, ".env"), "w") as f:
    f.write("\n")

os.environ["HERMES_HOME"] = d

from run_agent import AIAgent
agent = AIAgent(provider="custom", base_url="https://aigateway-sandbox.mspbots.ai/v1", model="gemini-3.1-pro-preview")
print("Agent api_key:", getattr(agent, "api_key", None))
