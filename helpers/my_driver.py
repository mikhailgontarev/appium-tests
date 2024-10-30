import time
from typing import Dict, Union

from appium.webdriver import Remote
from appium.webdriver.webelement import WebElement as MobileWebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from airtest.core.api import *

from img_element import ImageElement


class MyDriver(Remote):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device = init_device(platform=self.caps['platformName'])
        self.display_resolution = self.device.get_current_resolution()

    def wait_element(self, by: str = AppiumBy.ID, value: Union[str, Dict, None] = None, timeout=10) -> MobileWebElement:
        start_time = time.time()
        while time.time() < start_time + timeout:
            try:
                element = self.find_element(by, value)
                return element
            except NoSuchElementException:
                time.sleep(0.5)
        raise TimeoutError(f'Element {value} has not found in {timeout} sec.')

    def scroll_down(self):
        swipe((self.display_resolution[0] / 2, self.display_resolution[1] - 200),
              (self.display_resolution[0] / 2, 200))

    def scroll_up(self):
        swipe((self.display_resolution[0] / 2, 200),
              (self.display_resolution[0] / 2, self.display_resolution[1] - 200))

    def scroll_right(self):
        swipe((self.display_resolution[0] - 200, self.display_resolution[1] / 2),
              (200, self.display_resolution[1] / 2))

    def scroll_left(self):
        swipe((200, self.display_resolution[1] / 2),
              (self.display_resolution[0] - 200, self.display_resolution[1] / 2))

    @staticmethod
    def find_img_element(target) -> ImageElement | None:
        img_element_pos = exists(target)
        if not img_element_pos:
            return None
        else:
            return ImageElement(target, img_element_pos)

    @staticmethod
    def wait_img_element(target, timeout=None) -> ImageElement:
        img_element_pos = wait(v=target, timeout=timeout)
        return ImageElement(target, img_element_pos)
