import os
import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def app_config():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return {
        "ui_url": f"file://{os.path.join(base_dir, 'request', 'booking-demo.html')}",
        "api_url": "https://qa-booking-demo.vercel.app"
    }

@pytest.fixture(scope="function")
def booking_payload():
    return {
        "name": "Илья QA",
        "phone": "+7 (915) 393-33-08",
        "date": "2026-09-15",
        "time": "14:00",
        "guests": 4
    }

@pytest.fixture(scope="session")
def api_context(playwright: Playwright, app_config) -> APIRequestContext:
    request_context = playwright.request.new_context(
        base_url=app_config["api_url"],
        extra_http_headers={"Content-Type": "application/json"}
    )
    yield request_context
    request_context.dispose()
