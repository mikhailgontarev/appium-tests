
import json

import pytest
import subprocess

from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

from airtest.core.api import *
from helpers.my_driver import MyDriver
from app_images.app_elements import app_ui_elements


APPIUM_SERVER_URL = 'http://localhost:4723'


def pytest_addoption(parser):
    parser.addoption('--caps', default='android_capabilities')


@pytest.fixture(scope='session')
def get_capabilities(request):
    capabilities_file = request.config.getoption('caps')
    with open(os.path.join(os.path.dirname(__file__), f'../test_devices_capabilities/{capabilities_file}.json'), 'r') as f:
        capabilities = json.load(f)
    return capabilities


@pytest.fixture(scope='session')
def appium_server():
    my_env = os.environ.copy()
    my_env["ANDROID_HOME"] = os.path.expanduser('~/Library/Android/sdk')
    appium_process = subprocess.Popen('appium', env=my_env)
    time.sleep(2)   # Wait appium server starts

    yield APPIUM_SERVER_URL

    appium_process.kill()


@pytest.fixture()
def driver(get_capabilities, appium_server):
    driver = MyDriver('http://localhost:4723', options=UiAutomator2Options().load_capabilities(get_capabilities))

    #   Agree EULA dialog if it shows
    try:
        driver.wait_element(
            by=By.XPATH,
            value='//*[@resource-id="com.playrix.township:id/system_dialog_button" and @text="OK"]'
        ).click()
    except TimeoutError:
        pass

    # Agree using simulator (if tests run on simulator)
    if 'emulator' in get_capabilities['udid']:
        use_simulator_btn = None
        for _ in range(5):
            use_simulator_btn = driver.find_img_element(app_ui_elements.dialogs.keep_using_simulator)
            if use_simulator_btn:
                use_simulator_btn.click()
                break
            else:
                driver.scroll_down()
        assert use_simulator_btn, f'Button {app_ui_elements.dialogs.keep_using_simulator} has not found'

    yield driver

    driver.quit()
