
from appium.webdriver import Remote

from airtest.core.api import init_device


class MyDriver(Remote):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device = init_device(platform=self.caps['platformName'])
