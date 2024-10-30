
from airtest.core.api import *


class ImageElement:
    def __init__(self, template, position):
        self.reference_template = template
        self.position = position

    def is_visible(self):
        exists(self.reference_template)

    def click(self):
        touch(self.position)

    def drag_to(self, new_position):
        swipe(self.position, new_position)
