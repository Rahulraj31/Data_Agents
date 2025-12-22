from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
import google.auth



# Write modes define BigQuery access control of agent:
# ALLOWED: Tools will have full write capabilites.
# BLOCKED: Default mode. Effectively makes the tool read-only.
# PROTECTED: Only allows writes on temporary data for a given BigQuery session.


tool_config = BigQueryToolConfig(write_mode=WriteMode.ALLOWED)


  # Initialize the tools to use the credentials in the service account key.
creds, _ = google.auth.load_credentials_from_file("bq_agent_app/rahul-research-test-94ba79af556c.json")
credentials_config = BigQueryCredentialsConfig(credentials=creds)


bigquery_toolset = BigQueryToolset(credentials_config=credentials_config,   
#                                    tool_filter=[
)


# These are a set of tools aimed to provide integration with BigQuery, namely:

# list_dataset_ids: Fetches BigQuery dataset ids present in a GCP project.
# get_dataset_info: Fetches metadata about a BigQuery dataset.
# list_table_ids: Fetches table ids present in a BigQuery dataset.
# get_table_info: Fetches metadata about a BigQuery table.
# execute_sql: Runs a SQL query in BigQuery and fetch the result.
# forecast: Runs a BigQuery AI time series forecast using the AI.FORECAST function.
# ask_data_insights: Answers questions about data in BigQuery tables using natural language.




