import pytest
import asyncio
from app.core.order import create_order

@pytest.mark.asyncio
async def test_create_order():
    result = await create_order(1, 101)
    assert result["status"] == "success"