from pydantic_ai import Agent, RunContext
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from services import db_service
import os
from dotenv import load_dotenv

# This tells Python to read the .env file and load the variables into memory
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

# 2. Create the Provider and the Model explicitly
google_provider = GoogleProvider(api_key=API_KEY)
google_model = GoogleModel('gemini-3.5-flash', provider=google_provider)

# 3. Pass the explicit model to the Agent (no strings!)
agent = Agent(
    google_model, 
    system_prompt="You are a helpful store assistant for a brownie business. Use your tools to look up customer information."
)

@agent.tool
async def list_customers(ctx: RunContext) -> list[dict]:
    """List all customers."""
    return await db_service.get_all_customers()

@agent.tool
async def find_customer(ctx: RunContext, query: str) -> list[dict] | str:
    """Find a customer by name, email, or phone."""
    result = await db_service.find_customer_by_query(query)
    if not result:
        return f"No customer found matching '{query}'."
    return result