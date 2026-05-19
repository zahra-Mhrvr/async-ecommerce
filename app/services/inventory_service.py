# Inventory service logic
import asyncio


async def check_inventory(product_id: int) -> bool:
    await asyncio.sleep(1)

    # simple rule: even IDs are in stock
    return product_id % 2 == 0
