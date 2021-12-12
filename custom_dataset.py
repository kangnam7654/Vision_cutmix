import glob
import os

import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision.io import read_image

from utils.common.project_paths import GetPaths


class CutmixDataset(Dataset):
    def __init__(self):
        super().__init__()
        self.paths = GetPaths()

        self.data_list = glob.glob(self.paths.get_data_folder('train', '*.jpg'))

    def __len__(self):
        return len(self.data_list)

    def __getitem__(self, idx):
        img_path = self.data_list[idx]
        img = np.array(read_image(img_path))
        d, f = os.path.split(img_path)
        label = f.split('_')[0]
        return img, label


if __name__ == '__main__':
    dataset = CutmixDataset()
    loader = DataLoader(dataset, batch_size=1)
    for a, b in loader:
        print(b)
