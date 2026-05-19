import asyncio


async def get_customer(customer_id: int) -> dict:
    await asyncio.sleep(1)

    return {"id": customer_id, "name": f"Customer-{customer_id}"}
