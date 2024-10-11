
import json
import os

import pytest
import subprocess

from appium.options.android import UiAutomator2Options

from airtest.core.api import *
from airtest.core.helper import G
from helpers.my_driver import MyDriver


APPIUM_SERVER_URL = 'http://localhost:4723'


def pytest_addoption(parser):
    parser.addoption('--caps', default='android_capabilities')


@pytest.fixture(scope='session')
def get_capabilities(request):
    capabilities_file = request.config.getoption('caps')
    with open(os.path.join(os.path.dirname(__file__), f'devices_capabilities/{capabilities_file}.json'), 'r') as f:
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

    #   Agree EULA and continuing using simulator
    touch(wait(Template('OK.png')))
    display_resolution = driver.device.get_current_resolution()
    while not exists(Template('keep_using_simulator.png')):
        swipe((display_resolution[0] / 2, driver.device.get_current_resolution()[1] - 200),
              (display_resolution[0] / 2, 200))
    touch(Template('keep_using_simulator.png'))

    yield driver

    driver.quit()


@pytest.fixture(scope='module', autouse=True)
def add_images_location_path(request):
    G.BASEDIR.append((os.path.join(os.path.dirname(__file__), request.module.__name__.split('.')[-1])))
