
import os

from pathlib import Path

from app_images.main.main_screen_elements import MainScreen
from app_images.dialogs.dialogs_elements import Dialogs
from app_images.persons.persons_elements import Persons


class AppUIElements:

    def __init__(self):
        self._images_directory = Path(os.path.normpath(os.path.join(os.path.dirname(__file__), '../app_images/')))
        self.main_screen = MainScreen(self._images_directory)
        self.persons = Persons(self._images_directory)
        self.dialogs = Dialogs(self._images_directory)


app_ui_elements = AppUIElements()
