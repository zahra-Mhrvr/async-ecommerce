import requests

def test_health():
    r = requests.get("http://localhost:8000/health", timeout=5)
    assert r.status_code == 200