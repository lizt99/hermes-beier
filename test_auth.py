import sys, os
sys.path.insert(0, "/home/mspbots/.hermes/hermes-agent")
from hermes_cli.auth import resolve_api_key_provider_credentials
try:
    print(resolve_api_key_provider_credentials("custom"))
except Exception as e:
    print("Error:", e)
