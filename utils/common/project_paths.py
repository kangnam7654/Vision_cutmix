import os
from pathlib import Path


class GetPaths:
    def __init__(self):
        pass

    def get_project_root(self, *paths):
        root_dir = os.path.join(Path(__file__).parents[2], *paths)
        return root_dir

    def get_data_folder(self, *paths):
        data_folder = self.get_project_root('data', *paths)
        return data_folder
