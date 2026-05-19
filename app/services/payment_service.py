# Payment service logic
import asyncio


async def process_payment(customer: dict, amount: float) -> dict:
    await asyncio.sleep(2)

    if amount <= 0:
        return {"status": "failed", "reason": "invalid amount"}

    return {"status": "success", "customer": customer["name"], "charged": amount}
