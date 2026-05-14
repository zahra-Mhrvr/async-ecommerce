# Customer service logic
import asyncio

async def get_customer(customer_id):
    await asyncio.sleep(1)
    return {"id": customer_id, "name": "Alice"}