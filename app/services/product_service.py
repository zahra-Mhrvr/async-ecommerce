# Product service logic
import asyncio

async def get_product(product_id):
    await asyncio.sleep(2)
    return {"id": product_id, "price": 100}