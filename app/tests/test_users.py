import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_and_get_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Register
        res = await ac.post("/api/v1/users/", json={"email":"a@b.com","password":"secret"})
        assert res.status_code == 201
        data = res.json()
        assert data["email"] == "a@b.com"
        user_id = data["id"]

        # Get
        res2 = await ac.get(f"/api/v1/users/{user_id}")
        assert res2.status_code == 200
        assert res2.json()["email"] == "a@b.com"

@pytest.mark.asyncio
async def test_list_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/api/v1/users/")
        assert res.status_code == 200
        assert isinstance(res.json(), list)
