from google.adk.agents.llm_agent import Agent
from .tools import *
from .instructions import (
    root_agent_instruction
)
# cmd for server with reload and agent reload  adk web --reload --reload_agents -v
# swagger api after running adk api_server http://127.0.0.1:8000/docs

root_agent = Agent(
   model="gemini-2.5-flash",
   name="bigquery_agent",
   description=(
       "Agent that answers questions about BigQuery data by executing SQL queries"
   ),
   instruction=root_agent_instruction,
   tools=[bigquery_toolset]
)