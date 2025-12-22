from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.api_registry import ApiRegistry # pyright: ignore[reportMissingImports]


 # ---------------------- API Registory Tool GCP BQ MCP -----------------------
PROJECT_ID = "rahul-research-test"
MCP_SERVER_NAME = "projects/rahul-research-test/locations/global/mcpServers/google-bigquery.googleapis.com-mcp"

api_registry = ApiRegistry(PROJECT_ID)
registry_tools = api_registry.get_toolset(
    mcp_server_name=MCP_SERVER_NAME
)






#------------Data Viz Tool---------------------
import base64
import io
import matplotlib.pyplot as plt
import traceback

def render_plot_tool(code: str) -> str:
    """
    Executes Python code to generate a chart and returns it as a Base64 image.
    """
    print("--- Executing Chart Code ---")
    local_env = {}
    
    # Reset plot to prevent overlapping with previous charts
    plt.clf()
    
    try:
        # Execute the code
        exec(code, {}, local_env)
        
        # Save to buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight') # bbox_inches ensures labels aren't cut off
        buf.seek(0)
        
        # 1. ENCODE & CLEAN
        # .replace("\n", "") is CRITICAL. Without it, the image breaks in web chats.
        img_str = base64.b64encode(buf.read()).decode('utf-8').replace("\n", "")
        
        # 2. SAVE LOCAL COPY (Backup)
        # This guarantees you can see the result even if the web chat fails.
        with open("latest_chart.png", "wb") as f:
            f.write(base64.b64decode(img_str))
        print("Backup image saved to 'latest_chart.png'")

       # Return MARKDOWN syntax, not HTML
        return f"![Generated Chart](latest_chart.png)"
        
    except Exception as e:
        return f"Error executing plotting code: {traceback.format_exc()}"