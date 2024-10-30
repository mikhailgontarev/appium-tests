
from pathlib import Path

from airtest.core.cv import Template


class MainScreen:
    def __init__(self, root_path: Path):
        self._dir_name = root_path / 'main'
        self.empty_field = Template(self._dir_name / 'empty_field.png')
        self.sown_field = Template(self._dir_name / 'sown_field.png')
        self.wheat = Template(self._dir_name / 'wheat.png')
