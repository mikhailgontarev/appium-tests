
from pathlib import Path

from airtest.core.cv import Template


class Persons:
    def __init__(self, root_path: Path):
        self._dir_name = root_path / 'persons'
        self.ernie = Template(self._dir_name / 'Ernie.png')
