# Selene-in-Action

Учебный проект UI-автоматизации на Python с использованием **Selene** (обёртка над Appium/Selenium).  
Демонстрирует написание тестов для мобильных приложений (Android и iOS) через облачный сервис BrowserStack.

## 📌 Особенности

- **Android-тесты** — работают (BrowserStack, эмуляторы).
- **iOS-тесты** — **не работают** на Windows (невозможно загрузить и подписать IPA-файл).  
  Для iOS требуется macOS с Xcode.
- Используется **BrowserStack** для удалённого запуска (не требуется локальный Appium).
- Поддерживаются отчёты **Allure**.

## 🚀 Быстрый старт (Android)

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Waspish/selene-in-action.git
cd selene-in-action
```

### 2. Настройте виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Настройте BrowserStack (для Android)

В `tests/android-app/conftest.py` находятся ваши учётные данные `userName` и `accessKey`.  
**Убедитесь, что они актуальны** (замените на свои).

Если у вас нет аккаунта BrowserStack – зарегистрируйтесь и получите пробный период.

### 5. Запустите Android-тест

```bash
cd tests/android-app
pytest -s test_wikipedia.py
```

- Флаг `-s` показывает `print()` и логи BrowserStack.
- Тест проверит поиск в Wikipedia на Android-девайсе.

## ❗ Возможные проблемы

### Ошибка `BROWSERSTACK_INVALID_DEVICE`

Точное имя устройства должно совпадать со списком BrowserStack.  
Замените `deviceName` в `conftest.py` на корректное  


### Ошибка `BROWSERSTACK_INVALID_APP_URL`

ID приложения `bs://...` устарел. Загрузите своё Android-приложение через интерфейс BrowserStack и получите новый `app_url`.

## 🍏 iOS-тесты (предупреждение)

На **Windows** вы **не сможете** запустить iOS-тесты через BrowserStack, потому что:
- Требуется IPA-файл, который можно собрать только на macOS с Xcode.
- BrowserStack не позволяет загрузить IPA из Windows.

Если у вас есть Mac – вы можете:
- Собрать IPA в Xcode.
- Загрузить через App Automate → Upload.
- Использовать `app_url` в `capabilities` для iOS.

Код для iOS в репозитории приведён как пример, но на Windows он неработоспособен.

## 📦 Зависимости

Основные пакеты:

- `selene` – удобный API поверх Appium/Selenium
- `Appium-Python-Client` – клиент Appium
- `pytest` – фреймворк тестирования
- `pytest-xdist` – параллельный запуск
- `allure-pytest` – отчёты Allure
- `webdriver-manager` – управление драйверами (не используется при BrowserStack, но нужен для локальных запусков)