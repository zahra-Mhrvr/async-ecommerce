import asyncio

async def get_product(product_id: int) -> dict:
    await asyncio.sleep(1)

    return {
        "id": product_id,
        "name": f"Product-{product_id}",
        "price": 100 + product_id
    }