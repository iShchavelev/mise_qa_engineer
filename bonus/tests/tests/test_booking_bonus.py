import json
from playwright.sync_api import Page, APIRequestContext, expect

def test_ui_successful_booking_flow(page: Page, app_config, booking_payload):
    """Сквозной UI-тест: успешное заполнение и отправка формы."""
    # Открываем демо-страницу
    page.goto(app_config["ui_url"])
    
    # Заполняем форму по нативным селекторам полей
    page.fill("input[name='name']", booking_payload["name"])
    page.fill("input[name='phone']", booking_payload["phone"])
    page.fill("input[name='date']", booking_payload["date"])
    page.select_option("select[name='time']", booking_payload["time"])
    page.fill("input[name='guests']", str(booking_payload["guests"]))
    
    # Клик по кнопке отправки формы
    submit_btn = page.get_by_role("button", name="Забронировать")
    submit_btn.click()
    
    # Проверяем появление экрана успеха
    success_msg = page.locator("text=Бронь подтверждена")
    expect(success_msg).to_be_visible(timeout=5000)
    
    # Верифицируем, что введенное имя отображается в подтверждении
    expect(page.locator(f"text={booking_payload['name']}")).to_be_visible()


def test_api_successful_booking_endpoint(api_context: APIRequestContext, booking_payload):
    """Интеграционный API-тест: отправка POST-запроса на бэкенд."""
    # Выполняем POST-запрос через контекст Playwright API
    response = api_context.post(
        "/api/booking",
        data=json.dumps(booking_payload)
    )
    
    # Проверяем успешный статус ответа (200 или 201)
    assert response.ok, f"Запрос завершился с ошибкой. Код: {response.status}"
    assert response.status in (200, 201), f"Неожиданный статус-код: {response.status}"
    
    # Валидируем структуру вложенного JSON-ответа
    response_json = response.json()
    assert "booking" in response_json, "В корне JSON отсутствует объект 'booking'"
    
    booking = response_json["booking"]
    assert booking["name"] == booking_payload["name"]
    assert booking["phone"] == booking_payload["phone"]
    assert booking["date"] == booking_payload["date"]
    assert booking["time"] == booking_payload["time"]
    assert booking["guests"] == booking_payload["guests"]
    assert "id" in booking, "Сервер не сгенерировал уникальный ID бронирования"
