import asyncio

from app.services.customer_service import get_customer
from app.services.inventory_service import check_inventory
from app.services.payment_service import process_payment
from app.services.product_service import get_product


async def calculate_total_price(product):
    await asyncio.sleep(1)
    return product["price"] * 1.1


async def create_order(customer_id, product_id):
    customer_task = get_customer(customer_id)
    product_task = get_product(product_id)

    customer, product = await asyncio.gather(customer_task, product_task)

    in_stock = await check_inventory(product_id)

    if not in_stock:
        return {"status": "failed", "reason": "out_of_stock"}

    total_price = await calculate_total_price(product)

    payment = await process_payment(customer, total_price)

    return {
        "status": "completed",
        "payment": payment,
        "product": product,
        "customer": customer,
    }
