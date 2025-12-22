from google.adk.agents.llm_agent import Agent
from .mcp_gcp_tools import *
from google.genai import types
from google.adk.models.google_llm import Gemini
# cmd for server with reload and agent reload  adk web --reload --reload_agents -v
# swagger api after running adk api_server http://127.0.0.1:8000/docs

from .instructions import (
    root_agent_instruction, viz_agent_instruction
)

code_exec_config = types.GenerateContentConfig(
    tools=[types.Tool(code_execution=types.ToolCodeExecution())]
)


viz_agent = Agent(
    name="DataVisualizationAgent",
    model="gemini-2.5-flash",
    description="Generates charts and returns them as renderable images.",

    instruction=viz_agent_instruction,
    tools = [render_plot_tool]
)


root_agent = Agent(
   model="gemini-2.5-flash",
   name="bigquery_agent",
   description=(
       "Agent that answers questions about BigQuery data by executing SQL queries"
   ),
   instruction=root_agent_instruction,
   tools=[registry_tools],
   sub_agents=[viz_agent]

   
)