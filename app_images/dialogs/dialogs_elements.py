
from pathlib import Path

from airtest.core.cv import Template


class Dialogs:
    def __init__(self, root_path: Path):
        self._dir_name = root_path / 'dialogs'
        self.keep_using_simulator = Template(self._dir_name / 'keep_using_simulator.png')
