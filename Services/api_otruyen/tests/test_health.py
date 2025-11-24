import os
import sys

# Ensure the package root is on sys.path so tests can import `main` when pytest
# runs with the tests directory as the working directory.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import health_check
import asyncio
import json


def test_health_endpoint_returns_status():
    # Call the health handler directly to avoid testclient/ASGI incompatibilities
    resp = asyncio.run(health_check())

    # Accept both healthy (200) or unhealthy (503) — DB may be unavailable in CI
    assert hasattr(resp, "status_code")
    assert resp.status_code in (200, 503)

    # JSONResponse stores bytes in .body — decode & parse
    payload = json.loads(resp.body.decode()) if hasattr(resp, "body") else {}
    assert isinstance(payload, dict)
    assert "status" in payload