# Автоматизация тестирования (Bonus Tasks) — MISE Booking

В данном модуле реализованы бонусные задачи по автоматизации тестирования формы онлайн-бронирования. 

### Реализованный стек:
- **Pytest** — тестовый фреймворк.
- **Playwright (Python)** — моностек для сквозного UI-тестирования фронтенда и интеграционного API-тестирования бэкенда.

---

### 1. Быстрый запуск

```bash
# 1. Переходим в папку и создание изолированного виртуального окружения
cd bonus/tests
python -m venv .venv

# 2. Активация окружения:
# Для macOS/Linux:
#source .venv/bin/activate
# Для Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Для Windows (CMD):
#.venv\Scripts\activate.bat

# 3. Установка зависимостей
pip install -r requirements.txt

#4. Установка бинарников браузеров Playwright
#Для работы UI-тестов необходимо скачать системные зависимости браузера Chromium:
playwright install chromium

#5. Запуск тестового сьюта
#Запустите прогон UI и API сценариев:
pytest -v
```