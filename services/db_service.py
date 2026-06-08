from sqlalchemy import select
from database import AsyncSessionLocal
from app.models import Customer, Order

async def get_all_customers():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Customer))
        # Convert objects to dictionaries for the AI Agent
        customers = result.scalars().all()
        return [{"id": c.id, "name": c.name, "email": c.email, "phone": c.phone} for c in customers]

async def find_customer_by_query(query: str):
    async with AsyncSessionLocal() as session:
        stmt = select(Customer).where(
            (Customer.name.ilike(f"%{query}%")) | 
            (Customer.email.ilike(f"%{query}%")) | 
            (Customer.phone == query)
        )
        result = await session.execute(stmt)
        customers = result.scalars().all()
        return [{"id": c.id, "name": c.name, "email": c.email, "phone": c.phone} for c in customers]