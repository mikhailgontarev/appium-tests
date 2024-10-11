## Подготовка
### Установить пакеты для разработки

1. [Appium](https://appium.io/docs/en/2.2/quickstart/install/) для взаимодействия с мобильными устройствами
2. [Android Studio](https://developer.android.com/studio) для работы с Android устройствами (в том числе эмуляторами)
3. XCode на macos для работы с iOS устройствами
4. [pyenv](https://github.com/pyenv/pyenv) для установки требуемой версий питона

### Установка зависимостей
   ``` bash
   venv-install
   ```

## Запуск тестов
Обязательно указать в Makefile имя json-файла из папки devices_capabilities, с прописанными capabilities тестируемого устройства:
   ``` bash
   make test-smoke
   ```
либо напрямую из консоли:
``` bash
   ./test_venv/bin/python3 -m pytest tests --caps android_capabilities
   ```
